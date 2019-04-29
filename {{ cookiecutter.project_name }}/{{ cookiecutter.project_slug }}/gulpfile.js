let gulp          = require('gulp'),
    browserSync   = require('browser-sync').create(),
    concat        = require('gulp-concat'),
    del           = require('del'),
    gulpCopy      = require('gulp-copy'),
    cleanCSS      = require('gulp-clean-css'),
    uglify        = require('gulp-uglify-es').default,
    rename        = require('gulp-rename'),
    sass          = require('gulp-sass'),
    sourcemaps    = require('gulp-sourcemaps');


let output = 'assets/dist/',
    input = {
        css: [
            'node_modules/bootstrap/dist/css/bootstrap.css',

            'assets/source/css/*.css',
        ],
        sass: [
            'assets/source/scss/**/*.scss',
        ],
        img: [
            'assets/source/img/**/*',
        ],
        js: [
            'node_modules/jquery/dist/jquery.slim.js',
            'node_modules/popper.js/dist/popper.js',
            'node_modules/bootstrap/dist/js/bootstrap.bundle.js',

            'assets/source/js/*.js'
        ],
    };

gulp.task('clean', del.bind(null, [output]));

gulp.task('img', function () {
    return gulp.src(input.img)
        .pipe(gulp.dest(output + 'img/'));
});

gulp.task('css', function () {
    return gulp.src(input.css)
        .pipe(concat('plugins.css'))
        .pipe(gulp.dest(output + 'css/'));
});

gulp.task('sass', function () {
    return gulp.src(input.sass)
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        .pipe(sourcemaps.write('maps'))
        .pipe(gulp.dest('assets/dist/css'))
        .pipe(cleanCSS({compatibility: 'ie8'}))
        .pipe(rename({suffix: '-min'}))
        .pipe(gulp.dest('assets/dist/css'))
        .pipe(browserSync.stream())
});

gulp.task('js', function () {
    return gulp.src(input.js)
        .pipe(concat('plugins.js'))
        .pipe(gulp.dest('assets/dist/js'))
        .pipe(uglify())
        .pipe(rename({suffix: '-min'}))
        .pipe(gulp.dest('assets/dist/js'))
        .pipe(browserSync.stream())
});

gulp.task('watch', gulp.series('css', 'js', 'sass', 'img', function () {
    gulp.watch(input.css, gulp.series('css'));
    gulp.watch(input.sass, gulp.series('sass'));
    gulp.watch(input.js, gulp.series('js'));
    gulp.watch(input.img, gulp.series('img'));
}));

gulp.task('serve', gulp.series('css', 'js', 'sass', 'img', function () {
    browserSync.init({
        notify: false,
        proxy: "localhost:8000"
    });

    gulp.watch(input.css, gulp.series('css'));
    gulp.watch(input.sass, gulp.series('sass'));
    gulp.watch(input.js, gulp.series('js'));
    gulp.watch(input.img, gulp.series('img'));
    gulp.watch(['./**/*.{scss,css,html,py,js}']).on('change', browserSync.reload);
}));

gulp.task('build', gulp.series('css', 'js', 'sass', 'img'));

gulp.task('default', gulp.series('build'));
