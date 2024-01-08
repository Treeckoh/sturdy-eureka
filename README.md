Spotify Arduino IR controlled remote example.

Takes the input on an Arduino from the IR remote sensor, using the numeric values for a few commands.

Then prints to Serial a string to say which button has been pressed.

While the python script is ruhning, reads the serial and executes a request to the spotify api through the spotipy library.


For use change the client_id and client_secret variables in the spotify_auth file making sure the files are in the same directory.
