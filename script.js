// Função para verificar vulnerabilidade via API do HIBP
async function checkVulnerability(email) {
  const resultDiv = document.getElementById('result');
  resultDiv.innerHTML = 'Checking...';

  try {
    const response = await fetch(`http://localhost:3000/check-email?email=${encodeURIComponent(email)}`);
    const data = await response.json();

    if (data.breaches && data.breaches.length > 0) {
      resultDiv.innerHTML = `<p style="color: red;">⚠️ Your account is compromised!</p>`;
      data.breaches.forEach((breach) => {
        resultDiv.innerHTML += `<p><strong>${breach.Name}</strong>: ${breach.Description}</p>`;
      });
    } else {
      resultDiv.innerHTML = `<p style="color: green;">✅ Your account is secure!</p>`;
    }
  } catch (error) {
    resultDiv.innerHTML = `<p style="color: red;">Error checking your account. Please try again later.</p>`;
    console.error(error);
  }
}

// Event listener for form submission
document.getElementById('checkForm').addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent form reload
  const email = document.getElementById('emailInput').value.trim();
  checkVulnerability(email);
});