<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Liste des Matières</title>
    <link rel="stylesheet" href="css/style.css">
    <style>
    .notif {
        position: fixed;
        top: 30px; right: 30px;
        background: #2e7dff;
        color: #fff;
        padding: 16px 32px;
        border-radius: 6px;
        font-size: 1.1em;
        z-index: 9999;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15);
        opacity: 0.95;
        animation: fadein 0.5s;
    }
    .notif.error { background: #e74c3c; }
    .notif.success { background: #27ae60; }
    @keyframes fadein { from { opacity: 0; top: 0; } to { opacity: 0.95; top: 30px; } }

    .fab-btn {
        position: fixed;
        bottom: 36px;
        right: 36px;
        width: 56px;
        height: 56px;
        border-radius: 50%;
        background: #2e7dff;
        color: #fff;
        font-size: 2.2em;
        border: none;
        box-shadow: 0 2px 8px rgba(0,0,0,0.18);
        cursor: pointer;
        z-index: 1001;
        transition: background 0.2s;
    }
    .fab-btn:hover { background: #1b4fa0; }

    .modal-bg {
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(30,40,60,0.18);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 1002;
    }
    .modal-content {
        background: #fff;
        border-radius: 12px;
        box-shadow: 0 2px 24px rgba(0,0,0,0.18);
        padding: 32px 28px 24px 28px;
        min-width: 320px;
        position: relative;
        animation: fadein 0.3s;
    }
    .close-modal {
        position: absolute;
        top: 12px; right: 18px;
        font-size: 1.7em;
        color: #888;
        cursor: pointer;
    }
    .modal-content h2 {
        margin-bottom: 18px;
        color: #2e7dff;
        text-align: center;
    }
    .modal-content input {
        width: 100%;
        margin-bottom: 16px;
        padding: 10px;
        border-radius: 6px;
        border: 1px solid #bbb;
        font-size: 1em;
        background: #f6f8fa;
        transition: border 0.2s;
    }
    .modal-content input:focus {
        border: 1.5px solid #2e7dff;
        outline: none;
        background: #fff;
    }
    .modal-content button.btn {
        width: 100%;
        padding: 12px;
        background: #2e7dff;
        color: #fff;
        border: none;
        border-radius: 6px;
        font-size: 1.1em;
        font-weight: 600;
        cursor: pointer;
        transition: background 0.2s;
    }
    .modal-content button.btn:hover {
        background: #1b4fa0;
    }

    /* Confirmation stylisée */
    .custom-confirm-bg {
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(30,40,60,0.18);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 10010;
    }
    .custom-confirm-box {
        background: #fff;
        border-radius: 12px;
        box-shadow: 0 2px 24px rgba(0,0,0,0.18);
        padding: 32px 32px 24px 32px;
        min-width: 320px;
        text-align: center;
        position: relative;
        animation: fadein 0.3s;
    }
    .custom-confirm-box .confirm-title {
        font-size: 1.2em;
        font-weight: bold;
        margin-bottom: 14px;
        color: #53e73c;
    }
    .custom-confirm-box .confirm-message {
        margin-bottom: 22px;
        font-size: 1.05em;
        color: #333;
    }
    .custom-confirm-box .confirm-btns {
        display: flex;
        justify-content: center;
        gap: 18px;
    }
    .confirm-btn {
        padding: 10px 28px;
        border-radius: 6px;
        border: none;
        font-size: 1em;
        font-weight: 600;
        cursor: pointer;
        transition: background 0.2s;
    }
    .confirm-btn.yes {
        background: #53e73c;
        color: #fff;
    }
    .confirm-btn.yes:hover {
        background: #53e73c;
    }
    .confirm-btn.no {
        background: #f6f8fa;
        color: #333;
        border: 1px solid #bbb;
    }
    .confirm-btn.no:hover {
        background: #e0e7ff;
    }
    </style>
    <script>
    function notify(msg, type = "info") {
        let notif = document.createElement("div");
        notif.className = "notif " + type;
        notif.innerText = msg;
        document.body.appendChild(notif);
        setTimeout(() => notif.remove(), 3000);
    }

    // Nouvelle confirmation stylisée
    function showConfirm(action, onConfirm) {
        let old = document.getElementById("custom-confirm-bg");
        if (old) old.remove();

        let actionText = "";
        let color = "#e74c3c";
        if (action === "supprimer") {
            actionText = "Êtes-vous sûr de vouloir supprimer cette matière ?";
            color = "#e74c3c";
        } else if (action === "modifier") {
            actionText = "Êtes-vous sûr de vouloir modifier cette matière ?";
            color = "#f39c12";
        } else if (action === "créer") {
            actionText = "Êtes-vous sûr de vouloir créer cette matière ?";
            color = "#2e7dff";
        }

        let bg = document.createElement("div");
        bg.id = "custom-confirm-bg";
        bg.className = "custom-confirm-bg";
        let box = document.createElement("div");
        box.className = "custom-confirm-box";
        box.innerHTML = `
            <div class="confirm-title" style="color:${color};">Confirmation</div>
            <div class="confirm-message">${actionText}</div>
            <div class="confirm-btns">
                <button class="confirm-btn yes" id="confirm-yes">Oui</button>
                <button class="confirm-btn no" id="confirm-no">Non</button>
            </div>
        `;
        bg.appendChild(box);
        document.body.appendChild(bg);
        document.getElementById("confirm-yes").onclick = function() {
            bg.remove();
            onConfirm();
        };
        document.getElementById("confirm-no").onclick = function() {
            bg.remove();
        };
    }
    function confirmAction(action, url) {
        showConfirm(action, function() {
            window.location = url;
        });
        return false;
    }
    document.addEventListener("DOMContentLoaded", function() {
        var btn = document.getElementById("addMatiereBtn");
        if (btn) {
            btn.onclick = function() {
                document.getElementById("addMatiereModal").style.display = "flex";
            };
        }
    });

    function closeMatiereModal() {
        document.getElementById("addMatiereModal").style.display = "none";
    }

    function confirmCreate(e, formIdOrAction) {
    e.preventDefault();
    showConfirm('créer', function() {
        // Soumission du formulaire
        if (typeof formIdOrAction === "string") {
            // Si c'est un id de formulaire
            var form = e.target;
            if (form && form.submit) form.submit();
        }
    });
    return false;
}
    </script>
</head>
<body>
    <div class="sidebar">
        <h2>MonApp</h2>
        <a href="profil.jsp">🙍‍♂️ Profil</a>
        <a href="home.jsp">🏠 Accueil</a>
        <a href="matiere">📚 Voir les matières</a>
        <a href="compte">👤 Voir les comptes</a>
    </div>
    <div class="main-content">
        <div class="header">
            <h1>Liste des Matières</h1>
            <a href="home.jsp" class="btn">Retour à l'accueil</a>
        </div>
        <div class="content-box">
            <%
                String userRole = (String) session.getAttribute("role");
                if ("admin".equals(userRole)) {
            %>
            <!-- Bouton flottant + -->
            <button id="addMatiereBtn" class="fab-btn" title="Ajouter une matière">+</button>
            <!-- Modal d'ajout de matière -->
            <div id="addMatiereModal" class="modal-bg" style="display:none;">
                <div class="modal-content">
                    <span class="close-modal" onclick="closeMatiereModal()">&times;</span>
                    <h2>Ajouter une matière</h2>
                    <form id="addMatiereForm" method="post" action="matiere" onsubmit="return confirmCreate(event, 'matiere');">                        <input type="text" name="nom" placeholder="Nom de la matière" required>
                        <input type="number" name="nb_heures" placeholder="Nombre d'heures" required>
                        <button type="submit" class="btn">Ajouter</button>
                    </form>
                </div>
            </div>
            <%
                }
            %>
            <ul class="styled-list">
            <%
                java.util.List<model.Matiere> matieres = (java.util.List<model.Matiere>) request.getAttribute("matieres");
                if (matieres != null && !matieres.isEmpty()) {
                    for (model.Matiere m : matieres) {
            %>
                <li>
                    <span><%= m.getNom() %> (<%= m.getNbHeures() %>h)</span>
                    <span>
                        <% if ("admin".equals(userRole)) { %>
                        <a href="matiere?action=edit&id=<%= m.getId() %>" class="btn" onclick="return confirmAction('modifier', 'matiere?action=edit&id=<%= m.getId() %>')">✏️</a>
                        <a href="#" class="btn" onclick="return confirmAction('supprimer', 'matiere?action=delete&id=<%= m.getId() %>')">🗑️</a>
                        <% } %>
                    </span>
                </li>
            <%
                    }
                } else {
            %>
                <li>Aucune matière à afficher.</li>
            <%
                }
            %>
            </ul>
        </div>
    </div>
    <%
        String notif = request.getParameter("notif");
        if ("success_add".equals(notif)) {
    %>
    <script>notify("Matière ajoutée avec succès", "success");</script>
    <%
        } else if ("success_delete".equals(notif)) {
    %>
    <script>notify("Matière supprimée avec succès", "success");</script>
    <%
        } else if ("success_edit".equals(notif)) {
    %>
    <script>notify("Matière modifiée avec succès", "success");</script>
    <%
        }
    %>
</body>
</html>