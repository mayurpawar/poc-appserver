# Data to serve with our API
RELEASE_VERSIONS = {
    1: {
        "fversion": "1.0",
        "fdescription" : "First version released",
    },
    2: {
        "fversion": "2.0",
        "fdescription" : "Version API added",
    }
}

# Create a handler for our read (GET) version
def get_version():
    """
    This function responds to a request for /version
    with the complete lists of version

    :return:        sorted list of versions
    """
    # Create the list of versions from our data
    return [RELEASE_VERSIONS[key] for key in sorted(RELEASE_VERSIONS.keys())]