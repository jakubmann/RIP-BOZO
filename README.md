# RIP BOZO
A very simple script that sends you an email when someone dies.

## Configuration and running
You need to create a text file with the names of the people you want to be notified about, and also a text file containing email addresses of the recipients.
The app is using the GMAIL SMTP server, so you should configure `EMAIL_USER` and `EMAIL_PASS` environment variables in order for it to function. `EMAIL_USER` is a regular gmail address and `EMAIL_PASS` should be a GMAIL app password. You can learn how to create one [here](https://support.google.com/mail/answer/185833?hl=en-GB).

After configuring, you can run the app:
```console
$ python3 ripbozo.py names_file recipients_file
```

I highly recommend setting up a crontab.
