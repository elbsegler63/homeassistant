#!/usr/bin/env python3
"""
Simple validation script for Home Assistant YAML configuration files.
This script checks basic YAML syntax and structure.
"""

import yaml
import sys
import os
from pathlib import Path

def validate_yaml_file(file_path):
    """Validate a YAML file, ignoring Home Assistant specific tags."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Replace Home Assistant specific tags for basic validation
        content = content.replace('!include', '#include')
        content = content.replace('!include_dir_merge_named', '#include_dir_merge_named')
        content = content.replace('!secret', '#secret')
        
        # Try to parse as YAML
        yaml.safe_load(content)
        return True, "Valid YAML syntax"
        
    except yaml.YAMLError as e:
        return False, f"YAML Error: {e}"
    except Exception as e:
        return False, f"Error: {e}"

def main():
    """Main validation function."""
    base_path = Path(__file__).parent
    
    files_to_check = [
        'configuration.yaml',
        'template.yaml', 
        'dashboard_warmepumpe.yaml'
    ]
    
    print("🔍 Validating Home Assistant configuration files...")
    print("=" * 60)
    
    all_valid = True
    
    for file_name in files_to_check:
        file_path = base_path / file_name
        
        if not file_path.exists():
            print(f"❌ {file_name}: File not found")
            all_valid = False
            continue
            
        valid, message = validate_yaml_file(file_path)
        
        if valid:
            print(f"✅ {file_name}: {message}")
        else:
            print(f"❌ {file_name}: {message}")
            all_valid = False
    
    print("=" * 60)
    
    if all_valid:
        print("🎉 All configuration files have valid YAML syntax!")
        print("\n📋 Next steps:")
        print("1. Restart Home Assistant")
        print("2. Check if all sensors are available")
        print("3. Access the dashboard via 'Wärmepumpe' in the sidebar")
        return 0
    else:
        print("⚠️  Some configuration files have issues. Please fix them before restarting Home Assistant.")
        return 1

if __name__ == "__main__":
    sys.exit(main())