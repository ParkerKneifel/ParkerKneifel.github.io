<!DOCTYPE html>
<html>
<head>
    <title>1-Year Historical Returns</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <canvas id="historicalReturnsChart" width="400" height="200"></canvas>
    <script>
        // Generate random data with each month's data 0% to 30% higher than the previous month
        function generateHistoricalReturnsData() {
            let data = [100]; // Starting data point
            for (let i = 1; i < 12; i++) {
                let previousData = data[i - 1];
                let nextData = previousData * (1 + Math.random() * 0.3); // Increase by 0% to 30%
                data.push(nextData);
            }
            return data;
        }

        // Generate the x-axis labels for the year 2024
        function generateXAxisLabels() {
            let labels = [];
            for (let i = 0; i < 12; i++) {
                labels.push(`2024-${(i + 1).toString().padStart(2, '0')}`);
            }
            return labels;
        }

        // Chart.js configuration
        const ctx = document.getElementById('historicalReturnsChart').getContext('2d');
        const historicalReturnsChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: generateXAxisLabels(),
                datasets: [{
                    label: '1-Year Historical Returns',
                    data: generateHistoricalReturnsData(),
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                    fill: false
                }]
            },
            options: {
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: 'Month'
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'Return (%)'
                        }
                    }
                }
            }
        });
    </script>
</body>
</html>
