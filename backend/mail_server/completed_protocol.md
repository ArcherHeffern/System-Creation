CREATE <mailbox_name> # Creates a mailbox
Returns:
SUCCESS # on success
FAILURE # on failure

DELETE <mailbox_name> # Deletes a mailbox
Returns:
SUCCESS # on success
FAILURE # on failure

SEND <from> <to> <message...> # sends mail to mailbox
Returns:
SUCCESS # on success
FAILURE # on failure

RECIEVE <from>
Returns: List of messages of form
<from> <message> # on success
FAILURE # on failure

CLEAR <mailbox_name>
Returns:
SUCCESS # on success
FAILURE # on failure

DISCOVER
Returns:
<mailbox_name...> # Space seperated list of mailboxes
