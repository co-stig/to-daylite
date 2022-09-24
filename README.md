# To Daylite

Creates groups in Daylite, based on Direct Mail reports. It works with the server-side API and is designed
to run on a server.

A simple command-line app pulls contacts from Daylite and projects + reports from Direct Mail, then creates
groups in Daylite with the viewers (one group per report). This app is more of a working stub to build your
own automations on top of it.

## Usage

Install Python 3.x and import dependencies:

```sh
pip install -r requirements.txt
```

Generate Daylite and Direct Mail API tokens using their respective web UIs. Update `settings.ini` file with
those token IDs. Execute `main.py`:

```sh
python main.py
```

This program was tested on Debian Linux, but should work on macOS and Windows equally well.

## Known bugs and limitations

- The groups are created only for the email _viewers_. It's also possible to create groups for the contacts
who clicked the links.

- Downloading contacts is the most time-consuming operation. It is required to match emails to internal IDs,
which Daylite uses to create groups. Caching the list of contacts in a file would make subsequent executions
much faster.

- If you have Daylite application opened, it will pull the changes and update the list of groups in real time.
Sometimes it doesn't do it, then you should press Refresh once the script finishes execution.

- There might be API throttling on both Daylite and Direct Mail sides, but the docs are not very clear about
it.

## Credits

(C) Constantine Kulak, 2022.
