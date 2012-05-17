#include <stdio.h>
#include <midgard/midgard.h>

int main()
{
	midgard_init();

	MidgardConfig *config = midgard_config_new();
	g_object_set (config, 
			"dbtype", "SQLite", 
			"dbdir", "/tmp",
			"database", "MidgardStaticDB", 
			NULL);
	MidgardConnection *mgd = midgard_connection_new();
	midgard_connection_open_config (mgd, config, NULL);
	g_print("Connected '%s' \n", midgard_connection_get_error_string(mgd));

	midgard_storage_create_base_storage(mgd);
	g_print("Created storage: '%s' \n", midgard_connection_get_error_string(mgd));

	return 0;
}
