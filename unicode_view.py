import sublime, sublime_plugin

class UnicodeView(sublime_plugin.TextCommand):
    def run(self, edit):
        s = self.view.sel()
        if len(s) != 1 or s[0].size() != 1:
            sublime.error_message('Select 1 character only.')
        c = self.view.substr(s[0])
        o = ord(c)
        url = 'http://www.fileformat.info/info/unicode/char/%x/index.htm' % o
        print('opening %s' % url)
        self.view.window().run_command('open_url',
            {'url': url})
