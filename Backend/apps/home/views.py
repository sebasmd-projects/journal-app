from django.shortcuts import redirect
from django.views.generic import TemplateView, View
from django.http import HttpResponse

from .models import StartDescriptionModel, ContentIndexModel

# Create your views here.
INDEX_PATH = 'home/templates/index.html'
DOCUMENTATION_PATH = "home/templates/documentation.html"


class IndexTemplateView(TemplateView):
    template_name = INDEX_PATH

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)

        context['start_description'] = StartDescriptionModel.objects.all()

        context['content_index'] = ContentIndexModel.objects.all()

        return context


class DocumentationTemplateView(TemplateView):
    template_name = DOCUMENTATION_PATH


class SeeRequestsView(View):
    def get(self, request, *args, **kwargs):

        if request.user.is_superuser:
            
            # for h in request.headers:
            #     print('%s => {request.headers["%s"]}' % (h, h))

            # for k in request.META.keys():
            #     print('%s => {request.META["%s"]}' % (k, k))
                
            req = f""" 
            =========== USER INFO ===========
            user_id => {request.user.id}
            username => {request.user.username}
            email => {request.user.email}
            staff => {request.user.is_staff}
            superuser => {request.user.is_superuser}
            date_joined => {request.user.date_joined}
            full_name => {request.user.people.full_name}
            
            
            =========== REQUEST ===========
            Hypertext Transfer Protocol => {request.scheme}
            path => {request.path}
            path_info => {request.path_info}
            encoding => {request.encoding}
            content_type => {request.content_type}
            content_params => {request.content_params}
            cookies => {request.COOKIES}
            files => {request.FILES}
            session => {request.session}
            get_port => {request.get_port}
            method => {request.method}
            POST => {request.POST}
            GET => {request.GET}
            
            =========== HEADERS ===========
            Content-Length => {request.headers["Content-Length"]}
            Content-Type => {request.headers["Content-Type"]}
            Host => {request.headers["Host"]}
            Connection => {request.headers["Connection"]}
            Cache-Control => {request.headers["Cache-Control"]}
            Sec-Ch-Ua => {request.headers["Sec-Ch-Ua"]}
            Sec-Ch-Ua-Mobile => {request.headers["Sec-Ch-Ua-Mobile"]}
            Sec-Ch-Ua-Platform => {request.headers["Sec-Ch-Ua-Platform"]}
            Dnt => {request.headers["Dnt"]}
            Upgrade-Insecure-Requests => {request.headers["Upgrade-Insecure-Requests"]}
            User-Agent => {request.headers["User-Agent"]}
            Accept => {request.headers["Accept"]}
            Sec-Fetch-Site => {request.headers["Sec-Fetch-Site"]}
            Sec-Fetch-Mode => {request.headers["Sec-Fetch-Mode"]}
            Sec-Fetch-User => {request.headers["Sec-Fetch-User"]}
            Sec-Fetch-Dest => {request.headers["Sec-Fetch-Dest"]}
            Accept-Encoding => {request.headers["Accept-Encoding"]}
            Accept-Language => {request.headers["Accept-Language"]}
            Cookie => {request.headers["Cookie"]}
            
            =========== META ===========
            ALLUSERSPROFILE => {request.META["ALLUSERSPROFILE"]}
            APPDATA => {request.META["APPDATA"]}
            CHROME_CRASHPAD_PIPE_NAME => {request.META["CHROME_CRASHPAD_PIPE_NAME"]}
            COMMONPROGRAMFILES => {request.META["COMMONPROGRAMFILES"]}
            COMMONPROGRAMFILES(X86) => {request.META["COMMONPROGRAMFILES(X86)"]}
            COMMONPROGRAMW6432 => {request.META["COMMONPROGRAMW6432"]}
            COMPUTERNAME => {request.META["COMPUTERNAME"]}
            COMSPEC => {request.META["COMSPEC"]}
            DRIVERDATA => {request.META["DRIVERDATA"]}
            HOMEDRIVE => {request.META["HOMEDRIVE"]}
            HOMEPATH => {request.META["HOMEPATH"]}
            LOCALAPPDATA => {request.META["LOCALAPPDATA"]}
            LOGONSERVER => {request.META["LOGONSERVER"]}
            NUMBER_OF_PROCESSORS => {request.META["NUMBER_OF_PROCESSORS"]}
            ONEDRIVE => {request.META["ONEDRIVE"]}
            ORIGINAL_XDG_CURRENT_DESKTOP => {request.META["ORIGINAL_XDG_CURRENT_DESKTOP"]}
            OS => {request.META["OS"]}
            PATH => {request.META["PATH"]}
            PATHEXT => {request.META["PATHEXT"]}
            PROCESSOR_ARCHITECTURE => {request.META["PROCESSOR_ARCHITECTURE"]}
            PROCESSOR_IDENTIFIER => {request.META["PROCESSOR_IDENTIFIER"]}
            PROCESSOR_LEVEL => {request.META["PROCESSOR_LEVEL"]}
            PROCESSOR_REVISION => {request.META["PROCESSOR_REVISION"]}
            PROGRAMDATA => {request.META["PROGRAMDATA"]}
            PROGRAMFILES => {request.META["PROGRAMFILES"]}
            PROGRAMFILES(X86) => {request.META["PROGRAMFILES(X86)"]}
            PROGRAMW6432 => {request.META["PROGRAMW6432"]}
            PROMPT => {request.META["PROMPT"]}
            PSMODULEPATH => {request.META["PSMODULEPATH"]}
            PUBLIC => {request.META["PUBLIC"]}
            SESSIONNAME => {request.META["SESSIONNAME"]}
            SYSTEMDRIVE => {request.META["SYSTEMDRIVE"]}
            SYSTEMROOT => {request.META["SYSTEMROOT"]}
            TEMP => {request.META["TEMP"]}
            TMP => {request.META["TMP"]}
            USERDNSDOMAIN => {request.META["USERDNSDOMAIN"]}
            USERDOMAIN => {request.META["USERDOMAIN"]}
            USERDOMAIN_ROAMINGPROFILE => {request.META["USERDOMAIN_ROAMINGPROFILE"]}
            USERNAME => {request.META["USERNAME"]}
            USERPROFILE => {request.META["USERPROFILE"]}
            VIRTUAL_ENV => {request.META["VIRTUAL_ENV"]}
            VIRTUAL_ENV_PROMPT => {request.META["VIRTUAL_ENV_PROMPT"]}
            WINDIR => {request.META["WINDIR"]}
            ZES_ENABLE_SYSMAN => {request.META["ZES_ENABLE_SYSMAN"]}
            TERM_PROGRAM => {request.META["TERM_PROGRAM"]}
            TERM_PROGRAM_VERSION => {request.META["TERM_PROGRAM_VERSION"]}
            LANG => {request.META["LANG"]}
            COLORTERM => {request.META["COLORTERM"]}
            GIT_ASKPASS => {request.META["GIT_ASKPASS"]}
            VSCODE_GIT_ASKPASS_NODE => {request.META["VSCODE_GIT_ASKPASS_NODE"]}
            VSCODE_GIT_ASKPASS_EXTRA_ARGS => {request.META["VSCODE_GIT_ASKPASS_EXTRA_ARGS"]}
            VSCODE_GIT_ASKPASS_MAIN => {request.META["VSCODE_GIT_ASKPASS_MAIN"]}
            VSCODE_GIT_IPC_HANDLE => {request.META["VSCODE_GIT_IPC_HANDLE"]}
            _OLD_VIRTUAL_PATH => {request.META["_OLD_VIRTUAL_PATH"]}
            _OLD_VIRTUAL_PROMPT => {request.META["_OLD_VIRTUAL_PROMPT"]}
            DJANGO_SETTINGS_MODULE => {request.META["DJANGO_SETTINGS_MODULE"]}
            RUN_MAIN => {request.META["RUN_MAIN"]}
            SERVER_NAME => {request.META["SERVER_NAME"]}
            GATEWAY_INTERFACE => {request.META["GATEWAY_INTERFACE"]}
            SERVER_PORT => {request.META["SERVER_PORT"]}
            REMOTE_HOST => {request.META["REMOTE_HOST"]}
            CONTENT_LENGTH => {request.META["CONTENT_LENGTH"]}
            SCRIPT_NAME => {request.META["SCRIPT_NAME"]}
            SERVER_PROTOCOL => {request.META["SERVER_PROTOCOL"]}
            SERVER_SOFTWARE => {request.META["SERVER_SOFTWARE"]}
            REQUEST_METHOD => {request.META["REQUEST_METHOD"]}
            PATH_INFO => {request.META["PATH_INFO"]}
            QUERY_STRING => {request.META["QUERY_STRING"]}
            REMOTE_ADDR => {request.META["REMOTE_ADDR"]}
            CONTENT_TYPE => {request.META["CONTENT_TYPE"]}
            HTTP_HOST => {request.META["HTTP_HOST"]}
            HTTP_CONNECTION => {request.META["HTTP_CONNECTION"]}
            HTTP_CACHE_CONTROL => {request.META["HTTP_CACHE_CONTROL"]}
            HTTP_SEC_CH_UA => {request.META["HTTP_SEC_CH_UA"]}
            HTTP_SEC_CH_UA_MOBILE => {request.META["HTTP_SEC_CH_UA_MOBILE"]}
            HTTP_SEC_CH_UA_PLATFORM => {request.META["HTTP_SEC_CH_UA_PLATFORM"]}
            HTTP_DNT => {request.META["HTTP_DNT"]}
            HTTP_UPGRADE_INSECURE_REQUESTS => {request.META["HTTP_UPGRADE_INSECURE_REQUESTS"]}
            HTTP_USER_AGENT => {request.META["HTTP_USER_AGENT"]}
            HTTP_ACCEPT => {request.META["HTTP_ACCEPT"]}
            HTTP_SEC_FETCH_SITE => {request.META["HTTP_SEC_FETCH_SITE"]}
            HTTP_SEC_FETCH_MODE => {request.META["HTTP_SEC_FETCH_MODE"]}
            HTTP_SEC_FETCH_USER => {request.META["HTTP_SEC_FETCH_USER"]}
            HTTP_SEC_FETCH_DEST => {request.META["HTTP_SEC_FETCH_DEST"]}
            HTTP_ACCEPT_ENCODING => {request.META["HTTP_ACCEPT_ENCODING"]}
            HTTP_ACCEPT_LANGUAGE => {request.META["HTTP_ACCEPT_LANGUAGE"]}
            HTTP_COOKIE => {request.META["HTTP_COOKIE"]}
            wsgi.input => {request.META["wsgi.input"]}
            wsgi.errors => {request.META["wsgi.errors"]}
            wsgi.version => {request.META["wsgi.version"]}
            wsgi.run_once => {request.META["wsgi.run_once"]}
            wsgi.url_scheme => {request.META["wsgi.url_scheme"]}
            wsgi.multithread => {request.META["wsgi.multithread"]}
            wsgi.multiprocess => {request.META["wsgi.multiprocess"]}
            wsgi.file_wrapper => {request.META["wsgi.file_wrapper"]}
            CSRF_COOKIE => {request.META["CSRF_COOKIE"]}
                
            """
            return HttpResponse(req, content_type='text/plain', charset='latin-1')
        return redirect('auth/iniciar-sesion/?next=/ver-requests')