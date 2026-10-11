import os

file_path = "index.html"
anti_copy_script = """
<script>
// Protection ODM : Bloquer le clic droit et la copie du site
document.addEventListener('contextmenu', event => event.preventDefault());
document.addEventListener('keydown', event => {
    if (event.ctrlKey && (event.key === 'u' || event.key === 's' || event.key === 'c' || event.key === 'i')) {
        event.preventDefault();
    }
});
</script>
"""

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
    if "</head>" in html:
        html = html.replace("</head>", f"{anti_copy_script}\n</head>")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("✅ Pilier 1 Activé : Script anti-copie injecté avec succès.")
else:
    print("Fichier introuvable.")
