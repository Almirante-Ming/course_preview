import { Link } from "expo-router";
import { ImageBackground, StyleSheet, Text, TextInput, TouchableOpacity, View } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

export default function Register() {
  return (
    <ImageBackground 
      source={require('../assets/images/ado_sword.jpg')} 
      style={styles.backgroundImage} 
      resizeMode="cover"
    >
      <SafeAreaView style={styles.container}>
        <View style={styles.main_content}>
          <Text style={styles.title}>Create Your Account</Text>
          <Text style={styles.subtitle}>Join the adventure today</Text>
        </View>
        
        <View style={styles.form}>
          <View style={styles.inputGroup}>
            <Text style={styles.label}>Username</Text>
            <TextInput
              style={styles.input}
              placeholder="Enter your username"
              placeholderTextColor="rgba(255, 255, 255, 0.7)"
              autoCapitalize="none"
            />
          </View>

          <View style={styles.inputGroup}>
            <Text style={styles.label}>Email</Text>
            <TextInput
              style={styles.input}
              placeholder="Enter your email"
              placeholderTextColor="rgba(255, 255, 255, 0.7)"
              keyboardType="email-address"
              autoCapitalize="none"
            />
          </View>

          <View style={styles.inputGroup}>
            <Text style={styles.label}>Password</Text>
            <TextInput
              style={styles.input}
              placeholder="Create a password"
              placeholderTextColor="rgba(255, 255, 255, 0.7)"
              secureTextEntry
            />
          </View>

          <View style={styles.inputGroup}>
            <Text style={styles.label}>Confirm Password</Text>
            <TextInput
              style={styles.input}
              placeholder="Confirm your password"
              placeholderTextColor="rgba(255, 255, 255, 0.7)"
              secureTextEntry
            />
          </View>

          <TouchableOpacity style={styles.button}>
            <Text style={styles.buttonText}>Create Account</Text>
          </TouchableOpacity>

          <View style={styles.linkContainer}>
            <Text style={styles.linkText}>Already have an account? </Text>
            <Link href="/login" style={styles.link}>
              <Text style={styles.linkTextBold}>Sign In</Text>
            </Link>
          </View>
        </View>
      </SafeAreaView>
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
  backgroundImage: {
    flex: 1,
    width: '100%',
    height: '100%',
  },
  container: {
    flex: 1,
  },
  main_content: {
    position: 'absolute',
    top: '15%',
    left: 0,
    right: 0,
    zIndex: 1,
    alignItems: 'center',
    paddingHorizontal: 20,
  },
  title: {
    fontSize: 28,
    fontWeight: '900',
    color: '#00955cff',
    textAlign: 'center',
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 16,
    color: 'rgba(255, 255, 255, 0.9)',
    textAlign: 'center',
    fontWeight: '500',
  },
  form: {
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
    height: '70%',
    backgroundColor: 'rgba(70, 65, 65, 0.9)',
    padding: 30,
    paddingTop: 40,
    borderTopRightRadius: 90,
    borderTopLeftRadius: 20,
  },
  inputGroup: {
    marginBottom: 20,
  },
  label: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
    marginBottom: 8,
  },
  input: {
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.3)',
    borderRadius: 12,
    padding: 15,
    color: '#fff',
    fontSize: 16,
  },
  button: {
    backgroundColor: 'rgba(0, 149, 92, 0.8)',
    padding: 18,
    borderRadius: 12,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.3)',
    marginTop: 20,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: '700',
    textAlign: 'center',
  },
  linkContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 25,
  },
  linkText: {
    color: 'rgba(255, 255, 255, 0.8)',
    fontSize: 14,
  },
  link: {
    marginLeft: 4,
  },
  linkTextBold: {
    color: '#00955cff',
    fontSize: 14,
    fontWeight: '700',
  },
});
