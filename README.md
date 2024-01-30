# CStripper
Strip Cisco commands from Cisco Networking Labs

TO DO:
* Interactive prompt to load file from specified system path or filename
* Can the script be adapted to link command with specific lab task? ie can this script take the fluff out of the lab and return a condensed or paraphrased version of labs (some cisco labs are like 20 pages)
* Is this the most effective RegEx pattern to search in this context?
* What other RegEx patterns would be useful? Make them a hardcoded toggle or better yet, make an interactive prompt so user can select pattern to search from a list of human readable options
* Have the app take screenshots as input, then OCR the input to create workable data
* Use pexpect to auto configure devices in a running packet tracer file from stripped cisco labs
* argparse to create a companion experience for the lab using the stripped document
