from cook import water_is_boiling, water_starts_boiling , wait_x_minutes

# Das hier ist ein einzeiliger Kommentar
# benutzt die Funktionen water_is_boiling und wait_x_minutes
# um ein Ei zu kochen

if water_is_boiling():
    print("Das Wasser kocht!")
elif water_starts_boiling():
    print("Das Wasser fängt an zu kochen!")
else:
    print("Hier kocht noch nichts")
