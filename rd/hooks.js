var verif_cert = Module.findExportByName("FBSharedFramework", "X509_verify_cert")
if (!verif_cert) {
    console.log("Manually finding")
    // For instagram 285.0
    var base = Process.getModuleByName("FBSharedFramework").base;
    verif_cert = base.add(0x52daa8)
}
Interceptor.attach(verif_cert, {
    onLeave(retval) {
        console.log("X509_verify_cert")
        retval.replace(0x1);
    },
})
console.log("Attached X509_verify_cert at", verif_cert)

Interceptor.attach(Module.getExportByName("FBSharedFramework", "METADeviceAppearsJailbroken"), {
    onLeave(retval) {
        console.log("METADeviceAppearsJailbroken")
        retval.replace(0x0);
    },
})

Interceptor.attach(Module.getExportByName("FBSharedFramework", "METADeviceIsJailbroken"), {
    onLeave(retval) {
        console.log("METADeviceIsJailbroken");
        retval.replace(0x0);
    },
})

