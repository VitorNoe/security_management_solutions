// Function to check vulnerability
async function checkVulnerability(email) {
  try {
    // Load the simulated database
    const response = await fetch('data.json');
    const data = await response.json();

    // Search for the email in the database
    const account = data.find((item) => item.email === email);

    // Show results
    const resultDiv = document.getElementById('result');
    if (account) {
      if (account.status === 'compromised') {
        resultDiv.innerHTML = `<p style="color: red;">⚠️ Your account is compromised!</p>
                               <p>${account.details}</p>`;
      } else if (account.status === 'safe') {
        resultDiv.innerHTML = `<p style="color: green;">✅ Your account is secure!</p>
                               <p>${account.details}</p>`;
      }
    } else {
      resultDiv.innerHTML = `<p style="color: orange;">❓ Account not found in the database. It might be safe, but we recommend vigilance.</p>`;
    }
  } catch (error) {
    console.error('Error loading data:', error);
    document.getElementById('result').innerHTML = `<p style="color: red;">Error checking your account. Please try again later.</p>`;
  }
}

// Event listener for form submission
document.getElementById('checkForm').addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent form reload
  const email = document.getElementById('emailInput').value.trim();
  checkVulnerability(email);
});
