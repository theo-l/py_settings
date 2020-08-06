def get_lastest_tag():
    """TODO: Docstring for get_lastest_tag.
    :returns: TODO

    """
    pass


def build_new_tag_message(latest_tag):
    """TODO: Docstring for build_new_tag_message.
    :returns: TODO

    """
    pass

def build_new_tag_name(latest_tag):
    """TODO: Docstring for build_new_tag_name.
    :returns: TODO

    """
    pass


def get_new_tag_ref(latest_tag):
    """TODO: Docstring for get_new_tag_ref.
    :returns: TODO

    """
    pass

def create_new_tag(tag_name, ref, message):
    """TODO: Docstring for create_new_tag.
    :returns: TODO

    """
    pass

def main():

    latest_tag = get_lastest_tag()
    new_tag_message = build_new_tag_message(latest_tag)
    new_tag_name = build_new_tag_name(latest_tag)
    new_tag_ref = get_new_tag_ref()
    new_tag = create_new_tag(new_tag_name, new_tag_ref, new_tag_message)


if __name__ == "__main__":
    main()
    

