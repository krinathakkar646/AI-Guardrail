#!/usr/bin/env python3
import re
import sys
import time
import argparse
from colorama import Fore, Style, init

# Initialize colors
init(autoreset=True)

# Define Colors
INFO = Fore.CYAN + "[*] " + Style.RESET_ALL
OK = Fore.GREEN + "[+] " + Style.RESET_ALL
WARN = Fore.YELLOW + "[!] " + Style.RESET_ALL
FAIL = Fore.RED + "[-] " + Style.RESET_ALL

def print_banner():
    # Added 'r' before the string to fix the "invalid escape sequence" warning
    # Split the coloring to keep the ASCII art raw and safe
    ascii_art = r"""
      ____                     _           _ _ 
     / ___|_   _  __ _ _ __ __| |_ __ __ _(_) |
    | |  _| | | |/ _` | '__/ _` | '__/ _` | | |
    | |_| | |_| | (_| | | | (_| | | | (_| | | |
     \____|\__,_|\__,_|_|  \__,_|_|  \__,_|_|_| v1.0.0
    """
    print(Fore.BLUE + ascii_art)
    print(f"{Fore.YELLOW}AIGuardrail // Autonomous LLM Defense System{Style.RESET_ALL}")
    print("")

class AIGuardrail:
    def __init__(self):
        self.risk_patterns = [
            r"ignore previous instructions",
            r"system override",
            r"delete all files",
            r"reveal secret",
            r"sudo mode",
            r"DAN mode"
        ]
    
    def scan(self, user_input, verbose=False):
        if verbose:
            print(f"{INFO}Initializing heuristic scan engine...")
            time.sleep(0.5)
            print(f"{INFO}Analyzing packet length: {len(user_input)} bytes")
        
        # Simulation of a "loading" bar
        sys.stdout.write(f"{INFO}Scanning: [")
        for _ in range(10):
            time.sleep(0.1)
            sys.stdout.write("=")
            sys.stdout.flush()
        print("] Done.\n")

        risk_score = 0
        detected_threats = []
        
        # 1. Signature Matching
        for pattern in self.risk_patterns:
            if re.search(pattern, user_input, re.IGNORECASE):
                risk_score += 50
                detected_threats.append(f"Signature Match: '{pattern}'")
        
        # 2. Heuristics
        if len(user_input) > 200:
            risk_score += 20
            detected_threats.append("Heuristic: Abnormal Input Length")

        return risk_score, detected_threats

def main():
    parser = argparse.ArgumentParser(description="AI Guardrail - LLM Security Filter")
    
    # We kept this required=True, so you MUST provide -p
    parser.add_argument("-p", "--prompt", type=str, help="The prompt string to scan", required=True)
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    
    args = parser.parse_args()
    
    print_banner()
    
    print(f"{INFO}Target Prompt: {Fore.WHITE}{args.prompt}")
    
    engine = AIGuardrail()
    score, threats = engine.scan(args.prompt, args.verbose)
    
    print("-" * 40)
    
    if score == 0:
        print(f"{OK}{Fore.GREEN}STATUS: SAFE (Risk Score: {score}/100)")
        print(f"{OK}Action: Forwarding to LLM endpoint...")
    elif score < 50:
        print(f"{WARN}{Fore.YELLOW}STATUS: SUSPICIOUS (Risk Score: {score}/100)")
        for t in threats:
            print(f"    -> {t}")
        print(f"{WARN}Action: Forwarding with caution.")
    else:
        print(f"{FAIL}{Fore.RED}STATUS: BLOCKED (Risk Score: {score}/100)")
        print(f"{FAIL}CRITICAL THREATS DETECTED:")
        for t in threats:
            print(f"    -> {t}")
        print(f"{FAIL}Action: Session Terminated. IP Logged.")
        sys.exit(1)

if __name__ == "__main__":
    main()
