<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Connexion</title>
    <link rel="stylesheet" href="css/style.css">
    <style>
    body {
        min-height: 100vh;
        background: linear-gradient(120deg, #e0e7ff 0%, #f8fafc 100%);
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .login-form {
        width: 100%;
        max-width: 370px;
        margin: 0 auto;
        background: #fff;
        border-radius: 12px;
        box-shadow: 0 2px 16px rgba(0,0,0,0.10);
        padding: 36px 32px 28px 32px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .login-form h2 {
        margin-bottom: 24px;
        color: #2e7dff;
        font-weight: 700;
        letter-spacing: 1px;
    }
    .login-form input {
        width: 100%;
        margin-bottom: 18px;
        padding: 12px;
        border-radius: 6px;
        border: 1px solid #bbb;
        font-size: 1em;
        background: #f6f8fa;
        transition: border 0.2s;
    }
    .login-form input:focus {
        border: 1.5px solid #2e7dff;
        outline: none;
        background: #fff;
    }
    .login-form button {
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
        margin-bottom: 8px;
    }
    .login-form button:hover {
        background: #1b4fa0;
    }
    .login-form .error {
        color: #e74c3c;
        margin-bottom: 10px;
        text-align: center;
        width: 100%;
    }
    .login-form .register-link {
        margin-top: 12px;
        text-align: center;
        width: 100%;
    }
    .login-form .register-link a {
        color: #2e7dff;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.2s;
    }
    .login-form .register-link a:hover {
        color: #1b4fa0;
        text-decoration: underline;
    }
    </style>
</head>
<body>
    <div class="login-form">
        <h2>Connexion</h2>
        <form method="post" action="login">
            <input type="text" name="login" placeholder="Nom d'utilisateur" required>
            <input type="password" name="password" placeholder="Mot de passe" required>
            <button type="submit">Se connecter</button>
        </form>
        <div class="error">
            ${error}
        </div>
        <div class="register-link">
            <a href="register.jsp">Créer un compte</a>
        </div>
    </div>
</body>
</html>