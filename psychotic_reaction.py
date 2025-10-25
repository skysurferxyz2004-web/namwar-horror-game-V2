import time
import sys
import random

# --- 打字机效果输出 ---
def slow_print(text, delay=0.03, newline=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

# --- Enhanced Redaction Function with Dynamic Corruption ---
def redact(text, chance=0.15):
    result = ""
    corruption_symbols = ["█", "▓", "▒", "░", "#", "@", "%", "&", "?", "¥", "§", "¶", "†", "‡"]
    
    for c in text:
        if random.random() < chance and c.isalpha():
            result += random.choice(corruption_symbols[:4])  # Heavy redaction
        elif random.random() < 0.08:
            result += random.choice(corruption_symbols[4:])  # Light corruption
        elif random.random() < 0.02:
            result += random.choice(["\u2500", "\u2502", "\u25A0", "\u25A1"])  # Box drawing
        else:
            result += c
    return result

# --- Enhanced Psychological Horror System ---
def psychological_distortion():
    """Creates random psychological horror moments"""
    distortions = [
        "Your vision blurs momentarily. The text seems to rearrange itself.",
        "You hear a faint scratching from within the terminal speakers.",
        "The screen flickers. For a split second, you see your own reflection... but it's not moving with you.",
        "Static electricity makes your hair stand up. The air feels charged.",
        "You taste copper in your mouth. The cigarette ash falls onto the keyboard.",
        "Something moves in your peripheral vision. When you turn, nothing there.",
        "The temperature drops 5 degrees. Your breath becomes visible.",
        "You hear footsteps in the corridor above, but remember - the building is empty."
    ]
    if random.random() < 0.3:  # 30% chance of psychological distortion
        slow_print(f"\n[OPERATOR NOTE: {random.choice(distortions)}]\n", 0.02)
        time.sleep(1)

# --- Enhanced CIA Terminal Interface ---
slow_print("═══════════════════════════════════════════════════════════════════════════════", 0.01)
slow_print("█ CENTRAL INTELLIGENCE AGENCY // CLASSIFIED ARCHIVAL SYSTEM v2.1.7 █", 0.02)
slow_print("═══════════════════════════════════════════════════════════════════════════════", 0.01)
slow_print("INITIALIZING SECURE CONNECTION...", 0.03)
for i in range(3):
    slow_print(".", 0.5, False)
slow_print(" CONNECTED\n", 0.02)

slow_print("╔════════════════════════════════════════════════════════════════════════════╗", 0.01)
slow_print("║ SYSTEM STATUS: OPERATIONAL // CLEARANCE LEVEL: ALPHA-13 REQUIRED          ║", 0.02)
slow_print("║ LOCATION: LANGLEY, VIRGINIA // SECTOR 7 // ARCHIVE TERMINAL 003           ║", 0.02)
slow_print("║ DATE: 1983-07-14 // TIME: 23:48:33 EST // TEMPERATURE: 94°F               ║", 0.02)
slow_print("║ OPERATOR MODE: SINGLE USER // LAST ACCESS: 7 HRS 23 MIN AGO               ║", 0.02)
slow_print("║ WARNING: FILES FROM 1968-VN OPERATIONS REQUIRE SPECIAL HANDLING           ║", 0.02)
slow_print("║ NOTICE: PSYCHOLOGICAL EVALUATION RECOMMENDED POST-ACCESS                   ║", 0.02)
slow_print("╚════════════════════════════════════════════════════════════════════════════╝", 0.01)

# --- Operator Statement ---
operator_statement = [
    "[OPERATOR STATEMENT - AGENT ███████]",
    "──────────────────────────────────────────────────────────────────────────────",
    "You are a CIA investigative operative.",
    "It is a hot July night in 1983. The air in Langley hangs thick with heat and tension.",
    "Your superior slipped an old file into your hands—fifteen years of dust and silence.",
    "He said nothing, only that it was 'urgent.' Then he left quickly, closing the door behind him.",
    "Now the building is empty. The hum of fluorescent lights is the only sound.",
    "You light a Lucky Strike and begin your work.",
    "──────────────────────────────────────────────────────────────────────────────"
]

slow_print("\n")
for line in operator_statement:
    slow_print(line, 0.03)
slow_print("\n")


time.sleep(2)

# --- 输入探员姓名 ---
slow_print("╔════════════════════════════════════════════════════════════════════════════╗", 0.01)
slow_print("║                        AGENT AUTHENTICATION REQUIRED                      ║", 0.02)
slow_print("╚════════════════════════════════════════════════════════════════════════════╝", 0.01)
agent_name = input("\n> ENTER AGENT DESIGNATION: ").strip().upper()
if not agent_name:
    agent_name = "UNKNOWN"

slow_print(f"\n> AUTHENTICATING AGENT {agent_name}...", 0.04)
for i in range(5):
    slow_print(".", 0.3, False)
slow_print(" VERIFIED", 0.02)

slow_print(f"\n╔════════════════════════════════════════════════════════════════════════════╗", 0.01)
slow_print(f"║ WELCOME, AGENT {agent_name:<30} // ACCESS LEVEL: ALPHA-13                 ║", 0.02)
slow_print(f"║ SESSION INITIATED: {time.strftime('%H:%M:%S')} // AUTO-LOGOUT: 60 MINUTES ║", 0.02)
slow_print(f"║ SECURITY NOTICE: ALL ACTIONS LOGGED // PSYCH EVAL REQUIRED POST-SESSION   ║", 0.02)
slow_print(f"╚════════════════════════════════════════════════════════════════════════════╝", 0.01)

slow_print("\n> RETRIEVING CLASSIFIED FILES...", 0.04)
for i in range(3):
    slow_print("█", 0.5, False)
slow_print(" FILE LOCATED", 0.02)
psychological_distortion()
time.sleep(1.5)

# --- Enhanced File Display with Progressive Corruption ---
slow_print("\n" + "="*80, 0.01)
slow_print(" CLASSIFIED FILE // PROJECT: PSYCHOTIC REACTION // CLEARANCE: ALPHA-13 ".center(80), 0.02)
slow_print("="*80, 0.01)

psychological_distortion()

slow_print(redact("║ SUBJECT: PFC JUAN MARTINEZ // U.S.M.C. 26TH MARINE REGIMENT            ║"), 0.03)
slow_print(redact("║ STATUS: SOLE SURVIVOR // OPERATION ███████ // FEBRUARY 1968            ║"), 0.03)
slow_print(redact("║ LOCATION: KHE SANH REGION // DMZ // SOUTH VIETNAM                      ║"), 0.03)
slow_print(redact("║ CLASSIFICATION: FILE FRAGMENTS // FIELD DEBRIEF // ██████ REPORTS      ║"), 0.03)
slow_print(redact("║ WARNING: PSYCHOLOGICAL CONTENT // HANDLER DISCRETION ADVISED           ║"), 0.03)

psychological_distortion()

slow_print("\n> SYSTEM NOTICE: File corruption detected in 23.7% of segments.", 0.03)
slow_print("> NOTICE: Original interviewer - Dr. ████████ - declared missing 1983-06-██", 0.03)
slow_print("> WARNING: Previous agent assigned to case requested immediate transfer.", 0.03)
slow_print("\nThe terminal screen flickers as classified data streams across the monitor...", 0.03)
slow_print("\n" + "─"*80, 0.005)
time.sleep(2)

# --- 第一部分：春节攻势，Khe Sanh防御 ---
slow_print("FEBRUARY 3, 1968 – KHE SANH COMBAT BASE\n", 0.04)
slow_print("Mortar shells fall relentlessly. The base shudders under artillery fire.\n")
slow_print("Private MARTINEZ crouches behind sandbags, M16 trembling, sweat mixing with grime.\n")
slow_print("'CONTACT! EAST WALL!' screams the voice over the chaos.\n")
slow_print("The air thick with smoke, fire, and wet earth. Shadows move like predators.\n")
time.sleep(2)

slow_print("Hours stretch into darkness. Marines hold their ground.\n")
slow_print("Nearby bunker explodes, debris flies. Your ears ring.\n")
slow_print("Radio screams: 'Firebase Bravo! We're pinned! Requesting CAS—' static overtakes transmission.\n")
time.sleep(2)

slow_print("Finally, silence. Too much silence. The jungle feels... wrong.\n")
slow_print("From smoke emerges a figure. Eyes hollow, muttering prayers, uniform tattered.\n")
slow_print("Martinez calls out. No response. The figure fades into fog.\n")
time.sleep(2)

slow_print("Two days later, intelligence reports a downed C-47 transport 50 km west.\n")
slow_print("Captain briefs: 'Medical supplies. No risk.' His eyes flicker unease.\n")
slow_print("Twelve Marines, two door gunners, one UH-1 Huey. Jungle below stretches endlessly.\n")
time.sleep(2)

# --- 直升机出发 ---
slow_print("FEBRUARY 6, 1968 – EN ROUTE TO CRASH SITE\n", 0.04)
slow_print("Rotor blades slice mist. Canopy seems alive, whispering.\n")
slow_print("Crew chief yells: 'They say the bird went down carrying something... that's you, Martinez?'\n")
slow_print("1) Nod silently\n2) Ignore him\n")
choice_heli = input(">>> ").strip()

if choice_heli == "1":
    slow_print("Crew laughs nervously. 'Figures. Always some CIA bullshit.'\n")
else:
    slow_print("You ignore him. Engine roar swallows every word.\n")

slow_print("Lightning flashes. Something moves inside clouds. Vast, undefined.\n")
slow_print("Huey lurches. Instruments fail. Magnetic interference? Or something else?\n")
time.sleep(2)

slow_print("Horizon stabilizes. Pilot laughs. 'Just lightning.' But no one smiles.\n")
slow_print("Below, jungle pulses like a living organism.\n")
time.sleep(2)

# --- 坠机点 ---
slow_print("FEBRUARY 18, 1968 – NEAR KHE SANH, CRASH SITE\n", 0.04)
slow_print("C-47 broken across hillside. Tail embedded in foliage.\n")
slow_print("Parachutes flutter like tattered banners. Air reeks of decay.\n")
slow_print("Inside fuselage—no crew. Only dragging marks leading into shadows.\n")
slow_print("Whispers: 'Maybe they walked out...'\n'Or something dragged them,' Martinez murmurs.\n")
time.sleep(2)

# --- Enhanced Shadow Horror Loop ---
def shadow_manifestation():
    """Enhanced psychological horror sequence"""
    shadow_events = [
        "Movement detected in peripheral vision - analysis: INCONCLUSIVE",
        "Audio anomaly: whispers at frequency below human hearing threshold", 
        "Thermal variance: localized cold spot detected 3 feet behind operator",
        "Visual distortion: shadows appear to move independent of light sources",
        "Electromagnetic interference: slight fluctuation in monitor refresh rate",
        "Psychological note: operator pulse elevated 15% above baseline"
    ]
    
    slow_print("\n" + "▓"*80, 0.01)
    slow_print(" ENVIRONMENTAL ANOMALY DETECTED ".center(80), 0.02)
    slow_print("▓"*80, 0.01)
    
    for i, event in enumerate(shadow_events):
        slow_print(f"\n> SENSOR ALERT {i+1}: {event}", 0.03)
        psychological_distortion()
        time.sleep(1.2)
        
        if i == 2:  # Midpoint intensification
            slow_print("\n[SYSTEM WARNING: Unusual electromagnetic signatures detected]", 0.02)
            slow_print("[OPERATOR ADVISORY: Maintain focus on mission objectives]", 0.02)
            
    slow_print("\n> ANOMALY STATUS: Readings return to baseline parameters", 0.03)
    slow_print("> RECOMMENDATION: Continue file review with heightened awareness\n", 0.03)
    time.sleep(2)

# Call the enhanced shadow manifestation
shadow_manifestation()

slow_print("A sealed crate: 'CIA – PROPERTY OF PROJECT ████████'. Something taps inside.\n")
psychological_distortion()
slow_print("1) Open the crate\n2) Leave it sealed\n")
choice1 = input(">>> ").strip()

if choice1 == "1":
    slow_print("Lid creaks. Inside—a soaked burlap sack, pulsing faintly.\n")
    slow_print("It moves. Odor of rot and something unhuman.\n")
    slow_print("Private Harlow leans in—it bursts. Something once human crawls forth, twisted.\n")
else:
    slow_print("'Leave it,' you say. 'Airstrike will handle it.'\n")
    slow_print("Tapping grows louder. Matches your heartbeat.\n")

slow_print("Night falls. Platoon sets perimeter.\n")
slow_print("Jungle hums, then silence. Then—a scream. Wet, abrupt.\n")
time.sleep(2)

slow_print("Shapes emerge from fog. Faces of men thought dead, whispering your name.\n")
slow_print("'Martinez... come home.' Gunfire erupts. Chaos consumes clearing.\n")
time.sleep(2)

slow_print("Martinez grabs radio. Voice on other end is wrong.\n")
slow_print(redact("'This is ████████ Command. What you brought back... it's awake.'"), 0.02)
slow_print("Forest ignites. Screams vibrate the air, nonhuman in pitch.\n")
slow_print("Reality bends. Ground pulsates like flesh.\n")
time.sleep(2)

slow_print("1) Call for napalm strike\n2) Attempt to retreat to river\n")
choice2 = input(">>> ").strip()

if choice2 == "1":
    slow_print("'COMMAND, THIS IS MARTINEZ! FIRE MISSION! GRID 48-█!'\n")
    slow_print("Approved... God forgive you, son.\n")
    slow_print("Fire rains from sky. Shapes writhe in flames, still moving.\n")
    slow_print("When smoke clears, Martinez is alone.\n")
else:
    slow_print("You run for river. Water glows red under moonlight.\n")
    slow_print("Something rises—hands, mouths, eyes—all wrong.\n")
    slow_print("You fire until rifle melts. Then napalm falls anyway.\n")

time.sleep(2)

# --- 医院记录 ---
slow_print("\nRecording ends abruptly. Static fills screen.\n")
slow_print(redact("HOSPITAL RECORD: PVT MARTINEZ – SEVERE BURNS, HALLUCINATIONS, LOSS OF SPEECH."), 0.03)
slow_print(redact("FOLLOW-UP: INCIDENT AT FIELD HOSPITAL. UNKNOWN ASSAILANTS. RECORD TERMINATED."), 0.03)

# --- Psychological Reconstruction --- 
slow_print("\n[PSYCHOLOGICAL RECONSTRUCTION — SELECT FRAGMENTS]", 0.02)
slow_print("The following are stitched from Martinez's utterances and clinician notes. They are unedited.\n", 0.02)

fragments = [
    "'They came from the seams of the world. We didn't hear them until they were inside the alphabet of our heads.'",
    "'The radio taught me a number that tastes like metal: 07-██-██. I counted it until my teeth hurt.'",
    "'I saw Walker in a mirror that wasn't a mirror. He smiled, but smiled for the wrong months.'",
    "'Langley's lights are warm. Langley's cigarettes burn me. I remember the room, but not the doors.'",
    "'The crate remembers names. It hums them. You can hear the names under the drip of water.'",
    "'At night the trees open their mouths like drawers and spit out postcards from our childhoods. They are all bills.'"
]

for frag in fragments:
    slow_print(frag, 0.028)
    psychological_distortion()
    time.sleep(0.6)

psychological_distortion()

# --- Enhanced Terminal Shutdown Sequence ---
time.sleep(2)
slow_print("\n" + "█"*80, 0.01)
slow_print(" CRITICAL SYSTEM ERROR // SESSION TERMINATION IMMINENT ".center(80), 0.02)
slow_print("█"*80, 0.01)

slow_print("\n> SYSTEM STATUS: Multiple cascading failures detected", 0.03)
slow_print("> POWER GRID: Building electrical systems experiencing brownout", 0.03)
slow_print("> ENVIRONMENTAL: Temperature drop of 12 degrees in 30 seconds", 0.03)
slow_print("> SECURITY: Motion detectors triggered on floors 1, 3, 5, and 7", 0.03)
slow_print("> AUDIO: Unidentified breathing pattern detected behind operator position", 0.03)

psychological_distortion()

slow_print("\n[EMERGENCY PROTOCOL ACTIVATED]", 0.02)
slow_print("[OPERATOR ADVISORY: IGNITE EMERGENCY ILLUMINATION IF AVAILABLE]", 0.02)

slow_print("\nYour hand instinctively reaches for the Zippo lighter in your pocket.", 0.04)
slow_print("The metal is cold - colder than it should be in this heat.", 0.04)
slow_print("The wheel strikes. Orange flame dances, casting moving shadows on the walls.", 0.04)
slow_print("In the light, the file pages seem to shift and breathe on their own.", 0.04)

slow_print("\n> FINAL SYSTEM MESSAGE: ████████ PROTOCOL ACTIVATED ████████", 0.02)
slow_print("> SESSION LOG: ARCHIVED TO ████████ FOR REVIEW", 0.02)
slow_print("> PSYCHOLOGICAL EVALUATION: MANDATORY WITHIN 24 HOURS", 0.02)

slow_print("\n" + "▓"*80, 0.01)
slow_print(" END OF CHAPTER I // CASE FILE RETURNED TO VAULT ALPHA-13 ".center(80), 0.03)
slow_print("▓"*80, 0.01)

slow_print("\n\n[END OF CHAPTER 1]\n")