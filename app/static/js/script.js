document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("security-form");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
    const resultMessage = document.getElementById("result-message");
    const checkButton = document.getElementById("check-security");

    // Adiciona evento ao botão de verificação
    checkButton.addEventListener("click", async () => {
        const email = emailInput.value.trim();
        const password = passwordInput.value.trim();

        // Validação básica
        if (!email || !password) {
            displayMessage("Please fill in all fields.", "error");
            return;
        }

        try {
            // Chamada à API
            const response = await fetch("/api/verify-security", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ email, password }),
            });

            const data = await response.json();

            if (response.ok) {
                // Exibe a mensagem de sucesso
                displayMessage(data.message, "success");
            } else {
                // Exibe a mensagem de erro
                displayMessage(data.message || "An error occurred.", "error");
            }
        } catch (error) {
            console.error("Error:", error);
            displayMessage("Something went wrong. Please try again later.", "error");
        }
    });

    /**
     * Exibe mensagens no elemento de resultado.
     * @param {string} message - Mensagem a ser exibida.
     * @param {string} type - Tipo da mensagem: 'success' ou 'error'.
     */
    function displayMessage(message, type) {
        resultMessage.textContent = message;
        resultMessage.className = type; // Define a classe como 'success' ou 'error'
        resultMessage.classList.remove("hidden");
    }
});
