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
            <form id="investmentForm">
                <label for="portfolio1">Portfolio 1: </label>
                <input type="number" id="portfolio1" name="portfolio1" min="0" value="0"><br>

                <label for="portfolio2">Portfolio 2: </label>
                <input type="number" id="portfolio2" name="portfolio2" min="0" value="0"><br>

                <label for="portfolio3">Portfolio 3: </label>
                <input type="number" id="portfolio3" name="portfolio3" min="0" value="0"><br>

                <label for="portfolio4">Portfolio 4: </label>
                <input type="number" id="portfolio4" name="portfolio4" min="0" value="0"><br>

                <label for="portfolio5">Portfolio 5: </label>
                <input type="number" id="portfolio5" name="portfolio5" min="0" value="0"><br>

                <button type="submit">Submit</button>
            </form>
            <p id="timer" style="color: red; display: none;">You must wait 5 minutes before submitting again.</p>
            <p id="countdown" style="font-weight: bold; display: none;"></p>
        </section>

        <section id="portfolio-summary">
            <h2>Your Portfolio Summary</h2>
            <table id="portfolioTable" border="1">
                <thead>
                    <tr>
                        <th>Portfolio</th>
                        <th>Amount</th>
                    </tr>
                </thead>
                <tbody>
                </tbody>
            </table>
        </section>
    </main>

    <footer>
        <p>&copy; 2025 Investment Analysis Inc. All rights reserved.</p>
    </footer>

    <script>
        let lastSubmissionTime = null;
        let countdownInterval = null;

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
        new Chart(ctx, config);

        const database = [];

        function canSubmit() {
            if (!lastSubmissionTime) return true;
            const now = new Date();
            const diff = Math.floor((now - lastSubmissionTime) / 1000);
            return diff >= 300;
        }

        function startCountdown() {
            const countdownElement = document.getElementById('countdown');
            let timeLeft = 300;

            countdownElement.style.display = 'block';
            countdownInterval = setInterval(() => {
                timeLeft -= 1;
                countdownElement.textContent = `Time left: ${Math.floor(timeLeft / 60)}:${String(timeLeft % 60).padStart(2, '0')}`;

                if (timeLeft <= 0) {
                    clearInterval(countdownInterval);
                    countdownElement.style.display = 'none';
                }
            }, 1000);
        }

        function updatePortfolioSummary(investments) {
            const tableBody = document.getElementById('portfolioTable').querySelector('tbody');
            const row = document.createElement('tr');

            Object.keys(investments).forEach(portfolio => {
                const cell = document.createElement('td');
                cell.textContent = portfolio;
                row.appendChild(cell);

                const amountCell = document.createElement('td');
                amountCell.textContent = investments[portfolio];
                row.appendChild(amountCell);
            });

            tableBody.appendChild(row);
        }

        document.getElementById('investmentForm').addEventListener('submit', (event) => {
            event.preventDefault();

            if (!canSubmit()) {
                document.getElementById('timer').style.display = 'block';
                return;
            }

            document.getElementById('timer').style.display = 'none';

            const formData = new FormData(event.target);
            let totalInvestment = 0;
            let investments = {};

            formData.forEach((value, key) => {
                const amount = parseFloat(value) || 0;
                totalInvestment += amount;
                investments[key] = amount;
            });

            if (totalInvestment > 5) {
                alert('Total investment cannot exceed 5 units.');
                return;
            }

            database.push(investments);
            console.log('Current portfolio database:', database);
            updatePortfolioSummary(investments);

            lastSubmissionTime = new Date();
            startCountdown();

            alert('Investments submitted successfully!');
        });
    </script>
</body>
</html>
