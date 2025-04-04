import { View, Pressable, Text } from 'react-native';
import { btn_sty } from '../styles/btn_style';

type Props = {
  label: string;
};

export default function Button({ label }: Props) {
  return (
    <View style={btn_sty.buttonContainer}>
      <Pressable style={btn_sty.button} onPress={() => alert('You pressed a button.')}>
        <Text style={btn_sty.buttonLabel}>{label}</Text>
      </Pressable>
    </View>
  );
}