allSourceFiles = [
    'Gruntfile.coffee'
    'js/*.coffee'
]

module.exports = (grunt) ->
    pkg = grunt.file.readJSON 'package.json'

    grunt.initConfig
        staticRoot: 'static/fuselage/js'
        allSourceFiles: allSourceFiles
        pkg: pkg
        coffee:
            compile:
                files:
                    '<%= staticRoot %>/app.js': 'js/app.coffee'
        copy:
            main:
                files: [
                    {
                        expand: true
                        flatten: true
                        src: [
                            'bower_components/requirejs/require.js',
                            'bower_components/underscore/underscore.js'
                            'bower_components/jquery/jquery.js'
                            'node_modules/backbone/backbone.js'
                        ]
                        dest: '<%= staticRoot %>'
                    }
                ]


    grunt.loadNpmTasks 'grunt-contrib-coffee'
    grunt.loadNpmTasks 'grunt-contrib-uglify'
    grunt.loadNpmTasks 'grunt-contrib-copy'
    grunt.loadNpmTasks 'grunt-contrib-compress'
    grunt.loadNpmTasks 'grunt-contrib-concat'
    grunt.loadNpmTasks 'grunt-contrib-requirejs'
    grunt.registerTask 'default', [
        'coffee',
        'copy'
    ]
