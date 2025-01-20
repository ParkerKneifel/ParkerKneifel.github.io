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
            <p id="timer" style="color: red; display: none;">You must wait 20 seconds before submitting again.</p>
            <p id="countdown" style="font-weight: bold; display: none;"></p>
        </section>

        <section id="portfolio-summary">
            <h2>Your Portfolio Summary</h2>
            <div id="portfolioSummary">
                <p>Portfolio 1: <span id="summaryPortfolio1">0</span></p>
                <p>Portfolio 2: <span id="summaryPortfolio2">0</span></p>
                <p>Portfolio 3: <span id="summaryPortfolio3">0</span></p>
                <p>Portfolio 4: <span id="summaryPortfolio4">0</span></p>
                <p>Portfolio 5: <span id="summaryPortfolio5">0</span></p>
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
            let timeLeft = 20;

            countdownElement.style.display = 'block';
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
                const summaryElement = document.getElementById(`summary${portfolio.charAt(0).toUpperCase() + portfolio.slice(1)}`);
                summaryElement.textContent = investments[portfolio];
            });

            lastSubmissionTime = new Date();
            startCountdown();
            updateGraph();
            alert('Investments submitted successfully!');
        };

        const canSubmit = () => {
            if (!lastSubmissionTime) return true;
            const now = new Date();
            const diff = Math.floor((now - lastSubmissionTime) / 1000);
            return diff >= 20;
        };

        const updateGraph = () => {
            data.labels.push(`Month ${data.labels.length + 1}`);
            data.labels = data.labels.slice(-12);

            data.datasets.forEach(dataset => {
                dataset.data.push(Math.floor(Math.random() * 10 + 5)); // Random new return
                dataset.data = dataset.data.slice(-12);
            });

            portfolioChart.update();
        };

        const data = {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            datasets: [
                {
                    label: 'Portfolio 1',
                    data: [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                    borderColor: 'red',
                    fill: false
                },
                {
                    label: 'Portfolio 2',
                    data: [3, 4, 6, 7, 8, 10, 12, 13, 15, 16, 17, 18],
                    borderColor: 'blue',
                    fill: false
                },
                {
                    label: 'Portfolio 3',
                    data: [2, 3, 4, 6, 7, 8, 10, 11, 13, 14, 15, 16],
                    borderColor: 'green',
                    fill: false
                },
                {
                    label: 'Portfolio 4',
                    data: [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                    borderColor: 'orange',
                    fill: false
                },
                {
                    label: 'Portfolio 5',
                    data: [4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20],
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
                            text: 'Return (%)'
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
