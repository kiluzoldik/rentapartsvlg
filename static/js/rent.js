$(document).ready(function() {
    const bookedDates = [
        '2024-07-15',
        '2024-07-16',
        // Добавьте забронированные даты здесь
    ];

    function isDateBooked(date) {
        const dateString = $.datepicker.formatDate('yy-mm-dd', date);
        return bookedDates.includes(dateString);
    }

    $('#checkin-date, #checkout-date').datepicker({
        dateFormat: 'yy-mm-dd',
        beforeShowDay: function(date) {
            if (isDateBooked(date)) {
                return [false, 'ui-state-disabled'];
            } else {
                return [true, ''];
            }
        }
    });
});
