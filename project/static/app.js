new Vue({
    el: '#app',
    data: {
    orders: []
    },
    created: function () {
        const vm = this;
        axios.get('/api/orders/')
        .then(function (response) {
            console.log(response.data),
            vm.orders = response.data}
        )
    }
})
