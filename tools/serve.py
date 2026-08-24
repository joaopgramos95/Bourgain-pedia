#!/usr/bin/env python3
"""Serve the repository root over HTTP, with caching turned off.

The site ships its data as plain .js files that the builder rewrites in place
(site/data/*.js). Browsers cache those aggressively and heuristically -- there
is no Last-Modified-based revalidation to lean on when the URL never changes --
so after a rebuild the page keeps rendering yesterday's toolkit and yesterday's
open problems, with no clue that anything is stale. That has bitten this
project once already. Sending `Cache-Control: no-store` costs nothing on
localhost and means a rebuild is always one refresh away from being visible.

The document root is the repository, not site/, so that a link from a page to
material outside site/ -- a paper's digestion under <year>/<slug>/ -- resolves
the same way it does over file://.
"""
import functools
import http.server
import os
import sys


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, fmt, *args):        # quiet; the launcher detaches anyway
        pass


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8017
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
    handler = functools.partial(Handler, directory=os.path.abspath(root))
    with http.server.ThreadingHTTPServer(("", port), handler) as httpd:
        httpd.serve_forever()


if __name__ == "__main__":
    main()
