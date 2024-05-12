document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.btn-2019').addEventListener('click', function() {
        document.querySelector('.total-food-label').textContent = '25,315.545.';
        document.querySelector('.total-dry-food-label').textContent = '109165.645';
        document.querySelector('.total-wet-food-orders-label').textContent = '16149.9';
        document.getElementById('graph-image').src = 'img/19.png';
    });

    document.querySelector('.btn-2020').addEventListener('click', function() {
        document.querySelector('.total-food-label').textContent = '140,077.166.';
        document.querySelector('.total-dry-food-label').textContent = '46,147.666.';
        document.querySelector('.total-wet-food-orders-label').textContent = ' 0';
        document.getElementById('graph-image').src = 'img/20.png';
    });

    document.querySelector('.btn-19-20').addEventListener('click', function() {
        document.querySelector('.total-food-label').textContent = '229217.765';
        document.querySelector('.total-dry-food-label').textContent = '253122.36';
        document.querySelector('.total-wet-food-orders-label').textContent = '26156.9';
        document.getElementById('graph-image').src = 'img/19-20.png';
    });
});
