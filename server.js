const express = require('express');
const path = require('path');
const app = express();
const { exec } = require('child_process');
const bodyParser = require('body-parser');
const fs = require('fs');

// Middleware for parsing JSON and urlencoded form data
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Endpoint to handle form submission
app.post('/submit-form', (req, res) => {
    const formData = req.body; // Assuming form data is sent as JSON

    fs.writeFile('data.json', JSON.stringify(formData, null, 2), 'utf8', (err) => {
        if (err) {
            console.error(err);
            res.status(500).send('Error saving data');
            return;
        }

        exec('python similarity_matrix.py', (error, stdout, stderr) => {
            if (error) {
                console.error(`Error executing Python script: ${error.message}`);
                return;
            }
            if (stderr) {
                console.error(`Python script encountered an error: ${stderr}`);
                return;
            }
            console.log(`Python script output: ${stdout}`);


        });
    });
});

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

app.get('/get-csv-data/:csvId', (req, res) => {
    const csvId = req.params.csvId;
    const csvFiles = {
        'csv1': 'public/output.csv',
        'csv2': 'public/output_2.csv',
        'csv3': 'public/output_3.csv',
        'csv4': 'public/output_4.csv'
    };

    const csvFilePath = csvFiles[csvId];
    if (!csvFilePath) {
        res.status(404).send('CSV file not found');
        return;
    }

    fs.readFile(csvFilePath, 'utf8', (err, data) => {
        if (err) {
            console.error(err);
            res.status(500).send('Error reading CSV file');
            return;
        }

        res.send(data); // Send CSV data as a response
    });
});


const PORT = process.env.PORT || 2000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
