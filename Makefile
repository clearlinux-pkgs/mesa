PKG_NAME := mesa
URL = https://gitlab.freedesktop.org/mesa/mesa/-/archive/23ee6ca801cf9220dd544e6d659d683104f92c74/mesa-24.1+2703-g23ee6ca801c.tar.bz2
ARCHIVES = https://static.crates.io/crates/paste/paste-1.0.14.crate ./subprojects/paste-1.0.14 https://static.crates.io/crates/syn/syn-2.0.39.crate ./subprojects/syn-2.0.39 https://static.crates.io/crates/proc-macro2/proc-macro2-1.0.70.crate ./subprojects/proc-macro2-1.0.70 https://static.crates.io/crates/quote/quote-1.0.33.crate ./subprojects/quote-1.0.33 https://static.crates.io/crates/unicode-ident/unicode-ident-1.0.12.crate ./subprojects/unicode-ident-1.0.12

include ../common/Makefile.common
