#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define EXT_SUCCESS 0
#define EXT_ERR_TOO_MANY_ARGUMENTS 1
#define EXT_ERR_SOME_ERROR 2

#define CONFIG_GLOBAL_PATH "/etc/tamidshell"
#define CONFIG_XDG_PATH "$XDG_CONFIG_HOME/tamidshell"
#define CONFIG_HOME_PATH "$HOME/tamidshell"

struct Config {
    bool interactive;
    bool login;
    // I will add more to this section later
};

void config_init(struct Config *config) {
    config->interactive = false;
    config->login = false;
}

int parse_config(struct Config *config, char* path) {
    // TODO
    return 1;
}

int parse_args(struct Config *config, int argc, char** argv) {
    // TODO
    return 1;
}

int run_repl(struct Config *config) {
    // TODO
    printf("> ");
    return 1;
}

int main(int argc, char** argv, char** envp) {
    if (argc != 1) {
        fprintf(stderr, "USAGE: tamidsh");
        return EXT_ERR_TOO_MANY_ARGUMENTS;
    }
    struct Config config;
    config_init(&config);
    parse_config(&config, CONFIG_GLOBAL_PATH);
    parse_config(&config, CONFIG_XDG_PATH);
    parse_config(&config, CONFIG_HOME_PATH);
    parse_args(&config, argc, argv);

    // Repl logic
    if (run_repl(&config) == 0) {
        return EXT_ERR_SOME_ERROR;
    }

    return EXT_SUCCESS;
}