document.addEventListener('DOMContentLoaded', function() {
    // Constantes
    const API_URL = 'http://localhost:5000';
    
    // Elementos del DOM
    const fileInput = document.getElementById('csv-file');
    const fileInfo = document.getElementById('file-info');
    const querySection = document.querySelector('.query-section');
    const queryInput = document.getElementById('query-input');
    const resultsSection = document.getElementById('query-results');
    const viewLogsBtn = document.getElementById('view-logs');
    const logsContent = document.getElementById('logs-content');

    // Event Listeners
    fileInput.addEventListener('change', handleFileUpload);

    const executeBtn = document.getElementById('execute-query');
    executeBtn.addEventListener('click', async () => {
        const query = queryInput.value.trim();
        if (!query) {
            alert('Please enter a query');
            return;
        }

        try {
            const response = await fetch(`${API_URL}/query`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ query: query })
            });

            const data = await response.json();
            console.log('Query response:', data);  // Debug

            if (data.success) {
                displayResults(data.data,data.operation);
            } else {
                alert(data.message);
            }
        } catch (error) {
            console.error('Error executing query:', error);
            alert('Error executing query');
        }
    });

    viewLogsBtn.addEventListener('click', async () => {
        try {
            const response = await fetch(`${API_URL}/logs`);
            const data = await response.json();
            console.log('Logs response:', data); // Debug

            if (data.success) {
                // Mostrar los logs en una tabla
                logsContent.innerHTML = `
                    <table class="logs-table">
                        <thead>
                            <tr>
                                <th>Timestamp</th>
                                <th>Query</th>
                                <th>Browser</th>
                                <th>OS</th>
                                <th>Method</th>
                            </tr>
                        </thead>
                        <tbody>
                            ${data.data.map(log => `
                                <tr>
                                    <td>${log.timestamp}</td>
                                    <td>${log.query || 'N/A'}</td>
                                    <td>${log.browser} ${log.browser_version}</td>
                                    <td>${log.os} ${log.os_version}</td>
                                    <td>${log.method}</td>
                                </tr>
                            `).join('')}
                        </tbody>
                    </table>
                `;
                logsContent.classList.remove('hidden');
            } else {
                alert(data.message);
            }
        } catch (error) {
            console.error('Error fetching logs:', error);
            alert('Error fetching logs');
        }
    });

    // Manejadores de eventos
    async function handleFileUpload(e) {
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch(`${API_URL}/csv/upload`, {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        console.log('Parsed data:', data);

        if (data.success) {
            // Asegurar que los elementos existen
            const fileInfo = document.getElementById('file-info');
            const querySection = document.querySelector('.query-section');

            if (!fileInfo || !querySection) {
                console.error('Required elements not found');
                return;
            }

            // Mostrar información del archivo
            fileInfo.innerHTML = `
                <p>File loaded: ${file.name}</p>
                <p>Total rows: ${data.metadata.total_rows}</p>
                <p>Columns: ${data.metadata.columns.join(', ')}</p>
            `;
            
            // Remover clases hidden
            fileInfo.style.display = 'block';  // Alternativa a classList
            querySection.style.display = 'block';

            console.log('UI updated');  // Debug
        } else {
            alert(data.message || 'Error uploading file');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error uploading file');
    }
}

    async function executeQuery() {
        const query = queryInput.value.trim();
        if (!query) return;

        try {
            const response = await fetch(`${API_URL}/query`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query })
            });

            const data = await response.json();
            if (data.success) {
                displayResults(data.data,data.operation);
            } else {
                alert(data.message);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error executing query');
        }
    }

    function downloadAsCSV(data) {
        if (!data || !data.length) return;
        
        // Obtener headers de las columnas
        const headers = Object.keys(data[0]);
        
        // Crear contenido CSV
        const csvContent = [
            headers.join(','), // Header row
            ...data.map(row => headers.map(header => {
                // Manejar valores que puedan contener comas
                let value = row[header] ?? '';
                if (value.toString().includes(',')) {
                    value = `"${value}"`;
                }
                return value;
            }).join(','))
        ].join('\n');
        
        // Crear blob y descargar
        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'query_results.csv';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(url);
    }

    async function downloadFullCSV() {
        try {
            const response = await fetch(`${API_URL}/csv/download`);
            if (!response.ok) throw new Error('Download failed');
            
            const blob = await response.blob();
            const url = URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.download = 'updated_data.csv';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            URL.revokeObjectURL(url);
        } catch (error) {
            console.error('Error downloading CSV:', error);
            alert('Error downloading CSV');
        }
    }

    async function viewLogs() {
        try {
            const response = await fetch(`${API_URL}/logs`);
            const data = await response.json();
            
            if (data.success) {
                displayLogs(data.data);
            } else {
                alert(data.message);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error fetching logs');
        }
    }

    // Funciones auxiliares para mostrar resultados
    let currentOperation = null;
    function displayResults(data,queryType) {
        resultsSection.classList.remove('hidden');
        const resultsTable = resultsSection.querySelector('.results-table');
        const downloadBtn = document.getElementById('download-results');

        currentOperation = queryType;
        
        if(queryType === "SELECT"){
            lastQueryResults = data;
            downloadBtn.textContent = "Download Result as CSV";
            downloadBtn.classList.remove('hidden');
            const table = createTable(data);
            resultsTable.innerHTML = '';
            resultsTable.appendChild(table);
        }else{
            resultsTable.innerHTML = `<p>${data}</p>`;
            downloadBtn.textContent = "Download Update CSV";
            downloadBtn.classList.remove('hidden');
        }
    }
    document.getElementById('download-results').addEventListener('click', async () => {
        if (currentOperation === "SELECT") {
            downloadAsCSV(lastQueryResults);
        } else {
            downloadFullCSV();
        }
    });


    function createTable(data) {
        if (!data.length) {
            return document.createElement('p').textContent = 'No results found';
        }

        const table = document.createElement('table');
        
        // Crear encabezados
        const thead = document.createElement('thead');
        const headerRow = document.createElement('tr');
        Object.keys(data[0]).forEach(key => {
            const th = document.createElement('th');
            th.textContent = key;
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);
        table.appendChild(thead);

        // Crear filas de datos
        const tbody = document.createElement('tbody');
        data.forEach(row => {
            const tr = document.createElement('tr');
            Object.values(row).forEach(value => {
                const td = document.createElement('td');
                td.textContent = value;
                tr.appendChild(td);
            });
            tbody.appendChild(tr);
        });
        table.appendChild(tbody);

        return table;
    }

    function displayLogs(logs) {
        logsContent.classList.remove('hidden');
        logsContent.innerHTML = `
            <table>
                <thead>
                    <tr>
                        <th>Time</th>
                        <th>Query</th>
                        <th>Browser</th>
                        <th>OS</th>
                    </tr>
                </thead>
                <tbody>
                    ${logs.map(log => `
                        <tr>
                            <td>${log.timestamp}</td>
                            <td>${log.query || 'N/A'}</td>
                            <td>${log.browser}</td>
                            <td>${log.os}</td>
                        </tr>
                    `).join('')}
                </tbody>
            </table>
        `;
    }
});