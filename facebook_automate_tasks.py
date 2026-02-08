from playwright.sync_api import sync_playwright, TimeoutError
import time, os
from datetime import datetime

# ================= CONFIG =================
FILTER = "YOUR_POSTS"           # options: YOUR_POSTS, PHOTOS, VIDEOS
ACTIVITY_LOG_URL = f"https://www.facebook.com/me/allactivity/?category_key={FILTER}"
PROFILE_DIR = "fb_profile"      # persistent login
PROGRESS_FILE = "progress.txt"
SCREENSHOT_DIR = "screenshots"

DRY_RUN = False                 # True = no clicking
ARCHIVE_BEFORE = "2022-01-01"   # YYYY-MM-DD
# ==========================================

os.makedirs(SCREENSHOT_DIR, exist_ok=True)
CUTOFF_DATE = datetime.strptime(ARCHIVE_BEFORE, "%Y-%m-%d")

def save_progress(count):
    with open(PROGRESS_FILE, "w") as f:
        f.write(str(count))

def load_progress():
    if not os.path.exists(PROGRESS_FILE):
        return 0
    return int(open(PROGRESS_FILE).read().strip())

def screenshot(page, name):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"{SCREENSHOT_DIR}/{name}_{ts}.png"
    page.screenshot(path=path, full_page=True)
    print(f"📸 Screenshot saved: {path}")

def wait_for_logged_in(page):
    """Wait for a profile element or 2FA approval."""
    try:
        print("⏳ Waiting for login / 2FA approval...")
        page.wait_for_selector("div[aria-label='Your profile']", timeout=60000)
    except TimeoutError:
        print("❌ Login or 2FA not completed.")
        input("Press ENTER once logged in manually...")
        try:
            page.wait_for_selector("div[aria-label='Your profile']", timeout=60000)
        except TimeoutError:
            return False
    return True

def goto_activity_log(page):
    """Navigate safely to Activity Log."""
    for attempt in range(3):
        try:
            page.goto(ACTIVITY_LOG_URL, wait_until="networkidle")
            # Detect action menus dynamically
            page.wait_for_selector("div[aria-label*='Actions']", timeout=20000)
            return True
        except Exception as e:
            print(f"⚠️ Attempt {attempt+1} failed: {e}")
            screenshot(page, f"activity_log_fail_{attempt+1}")
            time.sleep(3)
    return False

# ------------------- MAIN -------------------
with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        PROFILE_DIR,
        headless=False,
        slow_mo=120
    )
    time.sleep(2)  # avoid TargetClosedError

    page = context.new_page()

    # ---------------- Login ----------------
    page.goto("https://www.facebook.com/")
    input("👉 Log in manually if first run or approve 2FA. Press ENTER once fully logged in...")
    if not wait_for_logged_in(page):
        context.close()
        exit()

    # ---------------- Activity Log ----------------
    if not goto_activity_log(page):
        print("❌ Could not open Activity Log. Exiting.")
        context.close()
        exit()

    archived_count = load_progress()
    print(f"▶️ Resuming from post #{archived_count}")
    print(f"📆 Archiving items before: {ARCHIVE_BEFORE}")
    print(f"🧪 Dry-run mode: {DRY_RUN}")
    print(f"📌 Filter: {FILTER}")

    scroll_round = 0
    while True:
        scroll_round += 1
        print(f"🔄 Scroll round {scroll_round}")

        try:
            menus = page.locator("div[aria-label*='Actions']")
            total = menus.count()
        except Exception as e:
            print("⚠️ Could not find post menus:", e)
            screenshot(page, f"menus_error_{scroll_round}")
            time.sleep(5)
            continue

        if archived_count >= total:
            page.mouse.wheel(0, 8000)
            time.sleep(5)
            continue

        for i in range(archived_count, total):
            try:
                menu = menus.nth(i)
                menu.click()
                page.wait_for_timeout(800)

                # Attempt to detect post date
                post_text = menu.locator("xpath=../../..").inner_text()
                post_date = None
                for token in post_text.split():
                    try:
                        dt = datetime.strptime(token, "%Y")
                        post_date = dt
                        break
                    except:
                        continue
                if post_date and post_date >= CUTOFF_DATE:
                    print("⏭️ Skipped (newer item)")
                    archived_count += 1
                    save_progress(archived_count)
                    continue

                if DRY_RUN:
                    print(f"🧪 Would archive item #{archived_count + 1}")
                else:
                    archive = page.locator("text=Move to archive").first
                    archive.wait_for(timeout=3000)
                    archive.click()
                    print(f"✅ Archived item #{archived_count + 1}")

                archived_count += 1
                save_progress(archived_count)
                time.sleep(3)

            except Exception as e:
                print(f"⚠️ Error on item #{archived_count + 1}: {e}")
                screenshot(page, f"error_item_{archived_count + 1}")
                time.sleep(5)
                continue

        page.mouse.wheel(0, 8000)
        time.sleep(5)
