import glob
print("osu! Song Grabber V0.0.1\nCreated by Ultrabear. June 30th, 2020")
maps = [i.replace("\\","/").split("/")[1] for i in glob.glob("Songs/*")]
outlist = []
for i in maps:
  try:
    outlist.append(int(i.split(" ")[0]))
  except ValueError:
    print(f"Did not parse: {i}")
with open("SongLinks.txt","w") as txt:
  for i in outlist:
    txt.write(f"https://osu.ppy.sh/beatmapsets/{i}\n")