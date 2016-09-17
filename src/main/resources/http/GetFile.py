#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

###################################################################################
#  Name: HTTP Get File
#
#  Description: Retrieve the content of file using HTTP GET.
#
#  Known Issues:
###################################################################################

import sys, string, urllib

if server is None:
    print "No server hostname provided."
    sys.exit(1)

host = { 'url': server }
request = HttpRequest(host, username, password)
response = request.get(uri)

if not response.isSuccessful():
    print "Failed to retrieve file from %s/%s" % (server, uri)
    response.errorDump()
    sys.exit(1)
else:
    fileContent = response.getResponse()
    print "Retrieved file content from %s/%s" % (server, uri)
