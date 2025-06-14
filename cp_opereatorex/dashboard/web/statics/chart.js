// Chart.js graph rendering for agent resource usage
function renderResourceChart(ctx, cpu, ram) {
    if (window.agentChart) window.agentChart.destroy();
    window.agentChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['CPU %', 'RAM %'],
            datasets: [{
                label: 'Resource Usage',
                data: [cpu, ram],
                backgroundColor: ['#36a2eb', '#ff6384']
            }]
        },
        options: {
            responsive: false,
            scales: {
                y: { beginAtZero: true, max: 100 }
            }
        }
    });
}