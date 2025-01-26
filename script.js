document.getElementById('security-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    if (!email || !password) {
        alert("Please fill in all fields!");
        return;
    }

    checkAccountSecurity(email, password);
});

function checkAccountSecurity(email, password) {
    // Simulação de análise de segurança
    const fakeData = [
        { email: "hacked@example.com", isSecure: false, message: "Your account has been hacked!" },
        { email: "safe@example.com", isSecure: true, message: "Your account is secure!" }
    ];

    const account = fakeData.find(data => data.email === email);

    if (account) {
        alert(account.message);
    } else {
        alert("Unable to verify your account. Please try another email.");
    }
}
