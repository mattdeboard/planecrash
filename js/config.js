require.config({
    baseUrl: "/js/lib",
    locale: "",
    shim: {
        underscore: {
            exports: "_"
        },
        backbone: {
            deps: ['underscore', 'jquery'],
            exports: 'Backbone'
        }
    },
    paths: {
        cs: '../bower_components/require-cs/cs',
        "coffee-script": "../bower_components/require-cs/coffee-script"
    }
});
