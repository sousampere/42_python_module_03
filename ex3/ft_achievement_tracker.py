#!/bin/bash/python3


survolt = {'Iron Belly', 'Time for Stew', 'How Did We Get Here?'}
poichigeon = {'Time to Farm!', 'Iron Belly', 'Kill the Beast!',
              'How Did We Get Here?'}
el_kiwi_masque = {'Iron Belly'}

print("🔥 Players achievements :"
      f"\nsurvolt: {survolt}"
      f"\npoichigeon: {poichigeon}"
      f"\nel_kiwi_masque: {el_kiwi_masque}\n"
      )

all_achivements = set.union(survolt, poichigeon, el_kiwi_masque)
print("🌍 Achievements shared by all players: "
      f"\n{set.intersection(poichigeon, el_kiwi_masque, survolt)}\n")

unique_achivements = all_achivements.difference(
    set.intersection(el_kiwi_masque, survolt, poichigeon)
    )
print("🌟 Ultra rare (unique) achievements: "
      f"\n{unique_achivements}\n"
      )

print("💁 All unlocked achivements :"
      f"\n{all_achivements}"
      f"\n(Total: {len(set.union(survolt, poichigeon, el_kiwi_masque))})\n")

print(f"Survolt vs Poichigeon common: {set.intersection(survolt, poichigeon)}")
print("Survolt's unique achivements: "
      f"{survolt.difference(poichigeon, el_kiwi_masque)}")
print("Poichigeon's unique achivements: "
      f"{poichigeon.difference(survolt, el_kiwi_masque)}\n")

print("❌ Missing achivements:"
      f"\nSurvolt: {all_achivements.difference(survolt)}"
      f"\nPoichigeon: {all_achivements.difference(poichigeon)}"
      f"\nel_kiwi_masque: {all_achivements.difference(el_kiwi_masque)}\n")

print("🏆 OG Players (that achieved \"How Did We Get Here?\"):")
og = {'How Did We Get Here?'}
if (len(og.intersection(el_kiwi_masque))):
    print("el_kiwi_masque")
if (len(og.intersection(survolt))):
    print("Survolt")
if (len(og.intersection(poichigeon))):
    print("Poichigeon")
