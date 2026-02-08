Iată un **ghid în limba română** ca să descarci și să folosești **repository-ul GitHub** de la
👉 [https://github.com/sversan/automate_facebook](https://github.com/sversan/automate_facebook) ([GitHub][1])

---

## 🧰 1) Ce trebuie să ai înainte

### 🔹 Linux / Mac / Windows

Trebuie să ai instalat:

1. **Git** – sistemul care descarcă codul de pe GitHub ([Gist][2])

   * pe **Linux**: în terminal rulezi `sudo apt install git` (exemplu pentru Ubuntu) ([Gist][2])
   * pe **Mac**: poți instala Git cu Homebrew (`brew install git`) sau când îți cere Xcode Command Line Tools ([Gist][2])
   * pe **Windows**: descarci „Git for Windows” de pe git-scm.com și îl instalezi ([Gist][2])

2. **Un terminal / linie de comandă:**

   * Linux → Terminal
   * Mac → Terminal
   * Windows → Git Bash sau PowerShell

3. **(Opțional) GitHub Desktop** – o aplicație grafică care te ajută să clonezi fără linia de comandă ([GitHub Docs][3])

---

## 📥 2) Cum descarci repository-ul

Repository-ul GitHub pe care vrei să îl descarci este:
➡️ **[automate_facebook pe GitHub](https://github.com/sversan/automate_facebook)**

### ❗ Varianta 1 – Folosind Git (CLI – recomandat)

Aceasta funcționează pe **Linux, Mac și Windows**:

1. Deschide o fereastră **terminal** (sau **Git Bash** pe Windows)

2. Mergi într-un director unde vrei să salvezi repository-ul:

   ```bash
   cd ~/Desktop
   ```

3. Clonează repository-ul cu comanda Git:

   ```bash
   git clone https://github.com/sversan/automate_facebook.git
   ```

4. Intră în folderul descărcat:

   ```bash
   cd automate_facebook
   ```

Acum ai tot conținutul proiectului pe calculatorul tău.

---

### 🧠 Ce s-ar putea întâmpla după descărcare

Repository-ul conține script-uri Python pentru „Python_Automate_Facebook_Tasks” ([GitHub][1]). Pentru a le rula probabil ai nevoie de:

✔️ Python instalat
✔️ Un mediu virtual (opțional)

Exemplu de pornire:

```bash
python3 -m venv env
source env/bin/activate   # pe Linux/Mac
env\Scripts\activate      # pe Windows
pip install -r requirements.txt   # dacă există
python facebook_automate_tasks.py
```

(*Fișierul `requirements.txt` nu e listat, dar dacă proiectul îl include, atunci folosești comanda de mai sus.*)

---

### ❗ Varianta 2 – Folosind GitHub Desktop (grafic)

Dacă nu vrei linie de comandă:

1. Descarcă și instalează **GitHub Desktop**:

   * Windows sau Mac: [https://desktop.github.com/download/](https://desktop.github.com/download/) ([GitHub][4])

2. Deschide GitHub Desktop și conectează-te cu contul tău GitHub.

3. În GitHub Desktop:

   * alege **File → Clone Repository**
   * lipește URL-ul: `https://github.com/sversan/automate_facebook.git`
   * apasă „Clone”

4. Repository-ul va fi descărcat într-un folder local.

---

## 📌 Recapitulare – Pași esențiali

| Pas | Ce faci                                                             |
| --- | ------------------------------------------------------------------- |
| 1   | Instalezi **Git**                                                   |
| 2   | Deschizi terminalul                                                 |
| 3   | Rulezi `git clone https://github.com/sversan/automate_facebook.git` |
| 4   | Intrii în folder și rulezi proiectul                                |

---

Dacă vrei, îți pot spune și **cum se rulează concret scriptul** (cu Python și eventual dependențe) — trebuie doar să îmi spui ce sistem de operare folosești (Linux, Mac sau Windows).

[1]: https://github.com/sversan/automate_facebook "GitHub - sversan/automate_facebook: Python_Automate_Facebook_Tasks"
[2]: https://gist.github.com/virgilwashere/17e99763b4f0c210486d5ece2befd5f8?utm_source=chatgpt.com "Installing Git on Linux, Mac OS X and Windows · GitHub"
[3]: https://docs.github.com/desktop/installing-and-configuring-github-desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop?utm_source=chatgpt.com "Installing GitHub Desktop - GitHub Docs"
[4]: https://desktop.github.com/download/?utm_source=chatgpt.com "Download GitHub Desktop | GitHub Desktop"
