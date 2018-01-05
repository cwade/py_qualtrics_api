py_qualtrics_api
==================

This package includes methods for using the Qualtrics API to:

* Copy a survey

* Delete a survey

* Activate a survey

* Create a mailing list

* Delete a mailing list

* Add contacts to a mailing list

* Generate unique survey links for members of a mailing list

* Create a message for the message library

* Distribute a survey to a mailing list using a message from the message library

----

Installation
------------

::

    pip install py_qualtrics_api


----

Overview
--------

Sample usage::

    import py_qualtrics_api.tools as pq
    import pandas as pd
    
    q = pq.QualtricsAPI('config.yml')

    # copy survey
    sid = q.copy_survey('SV_0abc05URqqrhMOO', 'My new survey')

    # delete survey
    success = q.delete_survey(sid)

    # copy survey, then activate the new survey
    sid = q.copy_survey('SV_0abc05URqqrhMOO', 'My new survey')
    success = q.activate_survey(sid)

    # create mailing list and add records from a Pandas dataframe
    # dataframe must contain an 'email' column (not case sensitive)
    # other optional special columns are: 'firstname', 'lastname',
    # 'externaldataref', 'unsubscribed' (defaults to false), 
    # 'language' (defaults to en)
    # none of these special column names are case sensitive, so 
    # ExTeRnAlDaTaRef would be acceptable
    mail_list = pd.read_csv('test_mailing_list.csv')
    ml_id = q.create_mailing_list('New mailing list',
                                  records_to_add=mail_list,
                                  list_category='API')

    # generate individual survey links for a mailing list
    # optional parameter link_type defaults to 'Individual' but other 
    # valid values are 'Multiple' and 'Anonymous'
    # return value is a pandas data frame of the core contact info with 
    # the following added columns: contactId, exceededContactFrequency,
    # 'link', 'linkExpiration', 'status', 'unsubscribed'
    links = q.get_links_for_mailing_list(sid, ml_id)

Sample config file (config.yml)::

    api_token: '4ru9we8fuper9ugergijergoijer34gierj876'
    data_center: 'co1'
    default_survey_owner: 'UR_3wjehoefof93s'
    default_library_owner: 'UR_3wjehoefof93s'

If you don't wish to store your API token in the configuration file, you can 
omit that line. If the API token isn't present in the configuration file, you 
will be prompted for it when you create a QualtricsAPI object.
