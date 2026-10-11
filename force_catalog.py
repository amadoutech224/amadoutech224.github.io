import os

file_path = "index.html"

# Le code complet, propre et parfaitement structuré pour ton agence internationale
html_prestige = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Amadou Tech — ODM | Agence Digitale & Haute Sécurité</title>
    <meta name="google-site-verification" content="4_QtDDwgZy4WZxzxaNMUDIB3_PFZ1IyCJjv9qbeBQ94" />
    <meta name="description" content="Amadou Tech — ODM. Agence digitale internationale et haute sécurisation web. Forfaits prestigieux de création de contenu et cyber-protection.">
    <meta property="og:title" content="Amadou Tech — ODM | Agence Digitale & Haute Sécurité">
    <meta property="og:description" content="Solution globale de haute performance web, cyber-protection et gestion de communauté par M. Amadou DIALLO.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://github.io">
    <style>
        :root { --bg-main: #0f172a; --bg-card: #1e293b; --accent-green: #38a169; --accent-blue: #3182ce; --text-light: #f1f5f9; --text-muted: #94a3b8; }
        body { font-family: 'Segoe UI', Roboto, sans-serif; background-color: var(--bg-main); color: var(--text-light); margin: 0; padding: 0; overflow-x: hidden; scroll-behavior: smooth; }
        a, button { transition: all 0.3s ease; text-decoration: none; }
        a:active, button:active { transform: scale(0.97) !important; opacity: 0.9 !important; }
        .container { max-width: 1100px; margin: 0 auto; padding: 0 20px; }
        
        .navbar { background-color: rgba(15, 23, 42, 0.9); backdrop-filter: blur(8px); position: fixed; top: 0; width: 100%; z-index: 1000; border-bottom: 1px solid #334155; box-sizing: border-box; }
        .nav-container { display: flex; justify-content: space-between; align-items: center; height: 70px; max-width: 1100px; margin: 0 auto; padding: 0 20px; }
        .logo { font-size: 1.4em; font-weight: bold; color: #fff; }
        .logo span { color: var(--accent-green); }
        .nav-links { display: flex; gap: 20px; align-items: center; }
        .nav-links a { color: var(--text-muted); font-weight: 500; font-size: 0.95em; }
        .nav-links a:hover { color: #fff; }
        .btn-client { background-color: var(--accent-blue); color: white; border: none; padding: 8px 16px; border-radius: 6px; font-weight: bold; cursor: pointer; font-size: 0.9em; }
        
        .hero { padding: 140px 0 60px 0; text-align: center; background: radial-gradient(circle at top, #1e293b 0%, #0f172a 100%); }
        .hero h1 { font-size: 2.5em; margin-bottom: 15px; }
        .hero p { color: var(--text-muted); max-width: 700px; margin: 0 auto 30px auto; font-size: 1.1em; line-height: 1.6; }
        
        .section-title { text-align: center; font-size: 2em; margin-bottom: 40px; position: relative; padding-bottom: 10px; }
        .section-title::after { content: ''; position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: 60px; height: 3px; background-color: var(--accent-green); }
        
        .services-grid { display: flex; flex-wrap: wrap; gap: 25px; justify-content: center; margin-bottom: 60px; }
        .service-card { background-color: var(--bg-card); padding: 30px; border-radius: 12px; flex: 1; min-width: 260px; max-width: 280px; border: 1px solid #334155; text-align: center; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4); }
        .service-card h3 { margin-top: 0; color: #fff; }
        .service-card .price { font-size: 1.8em; font-weight: bold; color: var(--accent-green); margin: 15px 0 20px 0; }
        .btn-order { display: block; width: 100%; text-align: center; background-color: var(--accent-green); color: white; padding: 12px; border-radius: 8px; font-weight: bold; box-sizing: border-box; }
        
        .method-flex { display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; margin: 40px 0; }
        .step-card { background-color: #141b2d; border-left: 4px solid var(--accent-blue); padding: 20px; border-radius: 0 8px 8px 0; flex: 1; min-width: 220px; }
        
        .faq-box { max-width: 750px; margin: 0 auto 60px auto; text-align: left; }
        .faq-item { background-color: var(--bg-card); padding: 20px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #334155; }
        .faq-item h4 { margin: 0 0 10px 0; color: #fff; }
        .faq-item p { margin: 0; color: var(--text-muted); font-size: 0.95em; line-height: 1.5; }

        .modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(15,23,42,0.85); z-index: 9999; justify-content: center; align-items: center; backdrop-filter: blur(5px); }
        .modal-content { background: #0f172a; border: 2px solid var(--accent-blue); padding: 35px; border-radius: 16px; width: 90%; max-width: 400px; }
    </style>
    <script>
    document.addEventListener('contextmenu', event => event.preventDefault());
    document.addEventListener('keydown', event => {
        if (event.ctrlKey && (event.key === 'u' || event.key === 's' || event.key === 'c' || event.key === 'i')) {
            event.preventDefault();
        }
    });
    </script>
</head>
<body>

    <nav class="navbar">
        <div class="nav-container">
            <div class="logo">Amadou Tech<span> — ODM</span></div>
            <div class="nav-links">
                <a href="#services">Services</a>
                <a href="#devis">Simulateur</a>
                <a href="#a-propos">À Propos</a>
                <button class="btn-client" onclick="ouvrirConnexionODM()">Espace Client</button>
            </div>
        </div>
    </nav>

    <header class="hero">
        <div class="container">
            <h1>Haute Performance Web & Cyber-Protection</h1>
            <p>L'écosystème digital haut de gamme conçu par M. Amadou DIALLO pour propulser l'image des leaders et sécuriser leurs actifs numériques à l'international.</p>
        </div>
    </header>

    <section id="services" style="padding: 60px 0;">
        <div class="container">
            <h2 class="section-title">Nos Prestations & Tarifs Internationaux</h2>
            <div class="services-grid">
                
                <div class="service-card">
                    <h3>Pack Visuels</h3>
                    <p style="color: var(--text-muted); font-size: 0.9em; min-height: 60px;">Création intensive de carrousels et de montages photos d'impact pour vos réseaux sociaux.</p>
                    <div class="price">19 €</div>
                    <a href="https://wa.me." class="btn-order">Commander</a>
                </div>

                <div class="service-card" style="border: 2px solid var(--accent-blue);">
                    <h3>Création Site Web</h3>
                    <p style="color: var(--text-muted); font-size: 0.9em; min-height: 60px;">Conception et déploiement complet de votre infrastructure internet professionnelle. Tarif fixe unique.</p>
                    <div class="price">325 €</div>
                    <a href="https://wa.me." class="btn-order" style="background-color: var(--accent-blue);">Commander la création</a>
                </div>

                <div class="service-card" style="border: 2px solid var(--accent-green); position: relative;">
                    <span style="position: absolute; top: -12px; left: 50%; transform: translateX(-50%); background: #38a169; color: white; padding: 2px 12px; border-radius: 10px; font-size: 0.75em; font-weight: bold;">PRESTIGE ANNUEL</span>
                    <h3 style="color: #fff; margin-top: 10px;">Gestion & Sécurité</h3>
                    <p style="color: var(--text-muted); font-size: 0.9em; min-height: 60px;">Cyber-protection continue 24/7, audits de code anti-piratage, création de contenu UGC et modération complète des réseaux sociaux.</p>
                    <div class="price">25 000 € / an</div>
                    <a href="https://wa.me." class="btn-order">Lancer le Forfait</a>
                </div>

            </div>
        </div>
    </section>

    <section style="padding: 60px 0; background-color: var(--bg-card);">
        <div class="container" style="text-align: center;">
            <h2 class="section-title">L'Impact ODM en Chiffres</h2>
            <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center;">
                <div style="background:#141b2d; padding:25px; border-radius:10px; min-width:240px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    <p style="color:#fe2c55; font-size:2.2em; font-weight:bold; margin:0;">+19 200</p>
                    <p style="margin:5px 0; font-weight:bold;">Abonnés sur TikTok</p>
                </div>
                <div style="background:#141b2d; padding:25px; border-radius:10px; min-width:240px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    <p style="color:var(--accent-green); font-size:2.2em; font-weight:bold; margin:0;">22,1 M</p>
                    <p style="margin:5px 0; font-weight:bold;">Vues globales cumulées</p>
                </div>
                <div style="background:#141b2d; padding:25px; border-radius:10px; min-width:240px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
git commit -m "Mise en ligne finale de la grille tarifaire en Euros"

git push origin main

rm force_catalog.py

git add index.html
git commit -m "Activation finale de la grille tarifaire internationale en Euros"
git push origin main

<meta name="google-site-verification" content="GWpKDetqvSZxEWntCqCW-3v-zEKhkzhkrUu1y2Hfclc" />cat << 'EOF' > fix_google_key.py
import os

file_path = "index.html"

# ⚠️ Colle ta balise exacte copiée sur ton écran entre les trois guillemets :
nouvelle_balise = """METS_ICI_LA_BALISE_COPIEE"""

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    # On cherche l'ancienne balise meta de vérification pour la remplacer proprement
    import re
    html_corrige = re.sub(r'<meta name="google-site-verification".*?/>', nouvelle_balise, html)
    
    # Si le nettoyage automatique ne trouve pas l'ancienne balise, on l'injecte sous le head
    if html_corrige == html:
        if "</head>" in html:
            html_corrige = html.replace("</head>", f"{nouvelle_balise}\n</head>")
        elif "</HEAD>" in html:
            html_corrige = html.replace("</HEAD>", f"{nouvelle_balise}\n</HEAD>")
            
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_corrige)
    print("✅ Correction effectuée : La clé de propriété Google exacte a été mise à jour.")
else:
    print("Fichier index.html introuvable.")
