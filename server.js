const express = require('express');
const axios = require('axios');
const cors = require('cors');
require('dotenv').config();

const app = express();
app.use(cors());
const PORT = process.env.PORT || 3000;

// Endpoint para verificar email na API HIBP
app.get('/check-email', async (req, res) => {
  const { email } = req.query;

  if (!email) {
    return res.status(400).json({ error: 'Email is required' });
  }

  try {
    const response = await axios.get(`https://haveibeenpwned.com/api/v3/breachedaccount/${email}`, {
      headers: {
        'hibp-api-key': process.env.HIBP_API_KEY,
        'User-Agent': 'Account-Vulnerability-Checker'
      }
    });

    res.json({ breaches: response.data });
  } catch (error) {
    if (error.response && error.response.status === 404) {
      res.json({ breaches: [] }); // Sem vazamentos encontrados
    } else {
      res.status(500).json({ error: 'Error checking the email' });
    }
  }
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
