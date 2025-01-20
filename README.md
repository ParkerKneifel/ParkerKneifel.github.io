<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Investment Portfolio</title>
    <link rel="stylesheet" href="styles.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <header>
        <h1>Investment Portfolio Analysis</h1>
    </header>

    <main>
        <section id="graph">
            <h2>1-Year Historical Returns</h2>
            <canvas id="portfolioChart" width="400" height="200"></canvas>
        </section>

        <section id="investment-selection">
            <h2>Select Your Investment</h2>
            <div id="investmentForm">
                <div>
                    <label>Portfolio 1: </label>
                    <button type="button" onclick="updateInvestment('portfolio1', 1)">+1</button>
                    <button type="button" onclick="updateInvestment('portfolio1', -1)">-1</button>
                    <span id="portfolio1Amount">0</span>
                </div>
                <div>
                    <label>Portfolio 2: </label>
                    <button type="button" onclick="updateInvestment('portfolio2', 1)">+1</button>
                    <button type="button" onclick="updateInvestment('portfolio2', -1)">-1</button>
                    <span id="portfolio2Amount">0</span>
                </div>
                <div>
                    <label>Portfolio 3: </label>
                    <button type="button" onclick="updateInvestment('portfolio3', 1)">+1</button>
                    <button type="button" onclick="updateInvestment('portfolio3', -1)">-1</button>
                    <span id="portfolio3Amount">0</span>
                </div>
                <div>
                    <label>Portfolio 4: </label>
                    <button type="button" onclick="updateInvestment('portfolio4', 1)">+1</button>
                    <button type="button" onclick="updateInvestment('portfolio4', -1)">-1</button>
                    <span id="portfolio4Amount">0</span>
                </div>
                <div>
                    <label>Portfolio 5: </label>
                    <button type="button" onclick="updateInvestment('portfolio5', 1)">+1</button>
                    <button type="button" onclick="updateInvestment('portfolio5', -1)">-1</button>
                    <span id="portfolio5Amount">0</span>
                </div>
                <div>
                    <p>Total: <span id="totalInvestment">0</span>/5</p>
                </div>
                <button type="button" id="submitButton" onclick="submitInvestments()">Submit</button>
            </div>
            <p id="timer" style="color: red; display: none;">You must wait 5 seconds before submitting again.</p>
            <p id="countdown" style="font-weight: bold; display: none;"></p>
        </section>

        <section id="portfolio-summary">
            <h2>Your Portfolio Summary</h2>
            <div id="portfolioSummary">
                <p>Portfolio 1: <span id="summaryPortfolio1">0.00</span></p>
                <p>Portfolio 2: <span id="summaryPortfolio2">0.00</span></p>
                <p>Portfolio 3: <span id="summaryPortfolio3">0.00</span></p>
                <p>Portfolio 4: <span id="summaryPortfolio4">0.00</span></p>
                <p>Portfolio 5: <span id="summaryPortfolio5">0.00</span></p>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2025 Investment Analysis Inc. All rights reserved.</p>
    </footer>

    <script>
        let lastSubmissionTime = null;
        let countdownInterval = null;
        const investments = {
            portfolio1: 0,
            portfolio2: 0,
            portfolio3: 0,
            portfolio4: 0,
            portfolio5: 0
        };
        const totalInvestments = {
            portfolio1: 0,
            portfolio2: 0,
            portfolio3: 0,
            portfolio4: 0,
            portfolio5: 0
        };

        const updateInvestment = (portfolio, change) => {
            const newAmount = investments[portfolio] + change;
            if (newAmount >= 0 && getTotalInvestment() + change <= 5) {
                investments[portfolio] = newAmount;
                document.getElementById(`${portfolio}Amount`).textContent = newAmount;
                document.getElementById('totalInvestment').textContent = getTotalInvestment();
            }
        };

        const getTotalInvestment = () => {
            return Object.values(investments).reduce((sum, value) => sum + value, 0);
        };

        const startCountdown = () => {
            const countdownElement = document.getElementById('countdown');
            let timeLeft = 5;

            countdownElement.style.display = 'block';
            countdownElement.textContent = `Time left: ${timeLeft}s`;

            countdownInterval = setInterval(() => {
                timeLeft -= 1;
                countdownElement.textContent = `Time left: ${timeLeft}s`;

                if (timeLeft <= 0) {
                    clearInterval(countdownInterval);
                    countdownElement.style.display = 'none';
                }
            }, 1000);
        };

        const submitInvestments = () => {
            if (!canSubmit()) {
                document.getElementById('timer').style.display = 'block';
                return;
            }

            document.getElementById('timer').style.display = 'none';

            const total = getTotalInvestment();
            if (total > 5) {
                alert('Total investment cannot exceed 5 units.');
                return;
            }

            Object.keys(investments).forEach(portfolio => {
                const investment = investments[portfolio];
                const portfolioIndex = parseInt(portfolio.replace('portfolio', '')) - 1;
                const lastReturn = allData[allData.length - 1][portfolioIndex] / 100;
                totalInvestments[portfolio] *= (1 + lastReturn);
                totalInvestments[portfolio] += investment;
                document.getElementById(`summary${portfolio.charAt(0).toUpperCase() + portfolio.slice(1)}`).textContent = totalInvestments[portfolio].toFixed(2);
                investments[portfolio] = 0;
                document.getElementById(`${portfolio}Amount`).textContent = 0;
            });

            document.getElementById('totalInvestment').textContent = 0;

            lastSubmissionTime = new Date();
            startCountdown();
            updateGraph();
        };

        const canSubmit = () => {
            if (!lastSubmissionTime) return true;
            const now = new Date();
            const diff = Math.floor((now - lastSubmissionTime) / 1000);
            return diff >= 5;
        };

        const generateRandomReturn = (previousData) => {
            return previousData * (1 + Math.random() * 0.3);
        };

        const constantData2024 = [
            { label: '2024-01', values: [10, 15, 20, 25, 30] },
            { label: '2024-02', values: [11, 16, 21, 26, 31] },
            { label: '2024-03', values: [12, 17, 22, 27, 32] },
            { label: '2024-04', values: [13, 18, 23, 28, 33] },
            { label: '2024-05', values: [14, 19, 24, 29, 34] },
            { label: '2024-06', values: [15, 20, 25, 30, 35] },
            { label: '2024-07', values: [16, 21, 26, 31, 36] },
            { label: '2024-08', values: [17, 22, 27, 32, 37] },
            { label: '2024-09', values: [18, 23, 28, 33, 38] },
            { label: '2024-10', values: [19, 24, 29, 34, 39] },
            { label: '2024-11', values: [20, 25, 30, 35, 40] },
            { label: '2024-12', values: [21, 26, 31, 36, 41] },
        ];

        let allLabels = constantData2024.map(item => item.label);
        let allData = constantData2024.map(item => item.values);
        let currentYear = 2025;
        let currentMonth = 1;

        const updateGraph = () => {
            const lastData = allData[allData.length - 1];

            if (currentMonth > 12) {
                currentMonth = 1;
                currentYear++;
            }
            const newLabel = `${currentYear}-${currentMonth.toString().padStart(2, '0')}`;
            currentMonth++;

            allLabels.push(newLabel);

            const newData = lastData.map(generateRandomReturn);
            allData.push(newData);

            if (allLabels.length > 12) {
                allLabels.shift();
                allData.shift();
            }

            portfolioChart.data.labels = allLabels.slice(-12);
            portfolioChart.data.datasets.forEach((dataset, index) => {
                dataset.data = allData.map(data => data[index] + totalInvestments[`portfolio${index + 1}`]).slice(-12);
                dataset.label = `Portfolio ${index + 1} (${(newData[index] - lastData[index]).toFixed(2)}%)`; // Update label with % increase
            });

            portfolioChart.update();
        };

        const data = {
            labels: allLabels.slice(-12),
            datasets: [
                {
                    label: 'Portfolio 1',
                    data: allData.map(data => data[0] + totalInvestments.portfolio1).slice(-12),
                    borderColor: 'red',
                    fill: false
                },
                {
                    label: 'Portfolio 2',
                    data: allData.map(data => data[1] + totalInvestments.portfolio2).slice(-12),
                    borderColor: 'blue',
                    fill: false
                },
                {
                    label: 'Portfolio 3',
                    data: allData.map(data => data[2] + totalInvestments.portfolio3).slice(-12),
                    borderColor: 'green',
                    fill: false
                },
                {
                    label: 'Portfolio 4',
                    data: allData.map(data => data[3] + totalInvestments.portfolio4).slice(-12),
                    borderColor: 'orange',
                    fill: false
                },
                {
                    label: 'Portfolio 5',
                    data: allData.map(data => data[4] + totalInvestments.portfolio5).slice(-12),
                    borderColor: 'purple',
                    fill: false
                }
            ]
        };

        const config = {
            type: 'line',
            data: data,
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                },
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
                            text: 'Total Value'
                        }
                    }
                }
            },
        };

        const ctx = document.getElementById('portfolioChart').getContext('2d');
        const portfolioChart = new Chart(ctx, config);
    </script>
</body>
</html>
