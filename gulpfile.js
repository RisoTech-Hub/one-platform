////////////////////////////////
// Setup
////////////////////////////////

// Gulp and package
const { parallel, series, watch } = require('gulp')

// Plugins
const browserSync = require('browser-sync').create()
const reload = browserSync.reload

////////////////////////////////
// Tasks
////////////////////////////////
// Browser sync server for live reload
function initBrowserSync() {
  browserSync.init(
    {
      // https://www.browsersync.io/docs/options/#option-open
      // Disable as it doesn't work from inside a container
      open: false,
      // https://www.browsersync.io/docs/options/#option-proxy
      proxy:  {
        target: 'django:8000', // Using Docker
        // target: 'localhost:8000', // Using Django
        proxyReq: [
          function(proxyReq, req) {
            // Assign proxy "host" header same as current request at Browsersync server
            proxyReq.setHeader('Host', req.headers.host)
          }
        ]
      }
    }
  )
}

// Watch
function watchPaths() {
  watch(['./**/*.{scss,css,html,py,js}']).on("change", reload)
}

// Set up dev environment
const dev = parallel(
  initBrowserSync,
  watchPaths
)

exports.default = series(dev)
exports["dev"] = dev
