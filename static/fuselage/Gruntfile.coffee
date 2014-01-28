allSourceFiles = [
    'Gruntfile.coffee'
    'js/*.coffee'
]

module.exports = (grunt) ->
    pkg = grunt.file.readJSON 'package.json'

    grunt.initConfig
        allSourceFiles: allSourceFiles
        pkg: pkg
        manifest: manifest

    grunt.loadNpmTasks 'grunt-contrib-coffee'
    grunt.loadNpmTasks 'grunt-contrib-uglify'
    grunt.loadNpmTasks 'grunt-contrib-copy'
    grunt.loadNpmTasks 'grunt-contrib-compress'
    grunt.loadNpmTasks 'grunt-contrib-concat'
    grunt.loadNpmTasks 'grunt-contrib-requirejs'
    grunt.registerTask 'default', [
        'coffee',
    ]
