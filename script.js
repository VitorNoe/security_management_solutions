// Function to simulate a security check
async function checkVulnerability(email) {
  const resultDiv = document.getElementById('result');
  resultDiv.innerHTML = '<p>Checking... 🔍</p>';

  // Simulated delay for API response
  await new Promise(resolve => setTimeout(resolve, 1500));

  // Simulated result
  const isCompromised = Math.random() > 0.5;

  if (isCompromised) {
    resultDiv.innerHTML = `
      <p class="compromised">⚠️ Your account is compromised!</p>
      <p>We recommend changing your password immediately and enabling 2FA.</p>
    `;
  } else {
    resultDiv.innerHTML = `
      <p class="safe">✅ Your account is secure!</p>
      <p>Keep using strong passwords and stay alert.</p>
    `;
  }
}

// Event listener for form submission
document.getElementById('checkForm').addEventListener('submit', (event) => {
  event.preventDefault();
  const email = document.getElementById('emailInput').value.trim();
  checkVulnerability(email);
});
