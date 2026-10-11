import os

file_path = "index.html"
speed_optimization = """
<script>
// Optimisation ODM : Chargement ultra-rapide des sections
document.addEventListener("DOMContentLoaded", function() {
    const images = document.querySelectorAll("img");
    images.forEach(img => { img.setAttribute("loading", "lazy"); });
    console.log("💎 Système ODM Speed en cours d'exécution...");
});
</script>
"""

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
    if "</body>" in html:
        html = html.replace("</body>", f"{speed_optimization}\n</body>")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("✅ Pilier 2 Activé : Optimisation de vitesse mondiale déployée.")
