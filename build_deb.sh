#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Name of the temporary workspace and the output file
BUILD_DIR="build_deb"
TARGET_DEB="fundamental-analysis_1.0.0_all.deb"

echo "🧹 Cleaning up old build artifacts..."
rm -rf $BUILD_DIR
rm -f $TARGET_DEB

echo "📁 Creating Debian package directory structure..."
mkdir -p $BUILD_DIR
# Copy the entire template structure (control file, wrapper scripts, etc.)
cp -r debian_layout/* $BUILD_DIR/

echo "🐍 Copying latest Python source code from src/..."
# Create the target directory inside the package and copy the Python package
mkdir -p $BUILD_DIR/usr/share/fundamental_analysis
cp -r fundamental_analysis/src/* $BUILD_DIR/usr/share/fundamental_analysis/

echo "🔐 Enforcing strict Debian file permissions..."
# 1. Set all directories to 755 (drwxr-xr-x)
find $BUILD_DIR -type d -exec chmod 755 {} +

# 2. Reset all files to 644 (rw-r--r--) to strip unexpected execution flags
find $BUILD_DIR -type f -exec chmod 644 {} +

# 3. Explicitly make the postinst script executable (Required for post-script execution)
if [ -f "$BUILD_DIR/DEBIAN/postinst" ]; then
    chmod 755 $BUILD_DIR/DEBIAN/postinst
fi

# 4. Explicitly make terminal binaries executable (rwxr-xr-x)
if [ -d "$BUILD_DIR/usr/bin" ]; then
    chmod 755 $BUILD_DIR/usr/bin/*
fi

echo "📦 Building the Debian package..."
dpkg-deb --build --root-owner-group $BUILD_DIR $TARGET_DEB

echo "✨ Success! The package was created as '$TARGET_DEB'."


